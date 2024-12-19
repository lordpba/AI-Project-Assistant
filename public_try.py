import streamlit as st
import os
import yaml
import json
import requests
import pandas as pd
from crewai import Agent, Task, Crew
from crewai_tools import BaseTool
from io import StringIO
import logging

# -- Title and Description --
st.title("✨ Trello Board Multi-Agent Analyzer ✨")
st.markdown("""
🔍 Analyze your Trello board using a multi-agent system powered by CrewAI.
⚙️ Configure your API keys below to get started.
""")

# -- Sidebar for API Keys --
st.sidebar.header("🔑 API Configuration")

# Input fields without saving capabilities
trello_api_key = st.sidebar.text_input("🔒 Trello API Key", type="password")
trello_token = st.sidebar.text_input("🔒 Trello Token", type="password")
openai_api_key = st.sidebar.text_input("🔒 OpenAI API Key", type="password")
trello_board_id = st.sidebar.text_input("🗂️ Trello Board ID")

# -- Load YAML Configurations --
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

agents_config = load_yaml('config/agents.yaml')
tasks_config = load_yaml('config/tasks.yaml')

# -- Custom Tools --
class BoardDataFetcherTool(BaseTool):
    name: str = "Trello Board Data Fetcher"
    description: str = "Fetches card data, comments, and activity from a Trello board."

    def _run(self) -> dict:
        url = f"https://api.trello.com/1/boards/{trello_board_id}/cards"
        query = {
            'key': trello_api_key,
            'token': trello_token,
            'fields': 'name,idList,due,dateLastActivity,labels',
            'attachments': 'true',
            'actions': 'commentCard'
        }
        response = requests.get(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch Trello data."}

# -- Logger Setup --
log_stream = StringIO()
logging.basicConfig(level=logging.INFO, stream=log_stream, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# -- Initialize Crew, Agents, and Tasks --
if st.sidebar.button("🚀 Analyze Board"):
    if not all([trello_api_key, trello_token, trello_board_id]):
        st.error("❌ Please provide all API credentials and Board ID.")
    else:
        # Create agents
        data_collection_agent = Agent(
            config=agents_config['data_collection_agent'],
            tools=[BoardDataFetcherTool()]
        )

        analysis_agent = Agent(
            config=agents_config['analysis_agent']
        )

        # Create tasks
        data_collection = Task(
            config=tasks_config['data_collection'],
            agent=data_collection_agent
        )

        data_analysis = Task(
            config=tasks_config['data_analysis'],
            agent=analysis_agent
        )

        report_generation = Task(
            config=tasks_config['report_generation'],
            agent=analysis_agent
        )

        # Create crew
        crew = Crew(
            agents=[data_collection_agent, analysis_agent],
            tasks=[data_collection, data_analysis, report_generation],
            verbose=True
        )

        # Redirect logs to StringIO
        logger.info("Starting Crew execution...")
        result = crew.kickoff()

        # Display logs
        st.subheader("📜 Log Output")
        st.text(log_stream.getvalue())

        # Display results
        st.subheader("📊 Report")
        st.markdown(result.raw)

        # Display Trello Data Summary
        trello_data = data_collection_agent.tools[0]._run()
        if "error" in trello_data:
            st.error("❌ Error fetching Trello data.")
        else:
            st.subheader("📋 Trello Task Summary")
            st.write(f"✅ Found {len(trello_data)} tasks on the Trello board.")
            st.dataframe(pd.DataFrame(trello_data))

        # Usage Metrics
        costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
        st.subheader("💰 Usage Metrics")
        st.write(f"💵 Total Costs: ${costs:.4f}")

        df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
        st.dataframe(df_usage_metrics)
