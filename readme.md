# Trello Board AI Multi-Agent Analyzer

✨ Welcome to the Trello Board Multi-Agent Analyzer ✨

<p align="center">
  <img src="assets/trello_analyzer.png" alt="Trello Board Multi-Agent Analyzer" width="500">
</p>

This application allows you to analyze your Trello board using a multi-agent system powered by CrewAI. Configure your API keys and get insights into your Trello boards like never before.

You can try quickly here --> https://8501-01jffe79g8564mbf4201va93c4.cloudspaces.litng.ai/

## Features

- 🔍 Analyze your Trello board with advanced multi-agent systems.
- ⚙️ Easy configuration of API keys through the sidebar.
- 📊 Visualize and manage your Trello data seamlessly.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/trello-analyzer.git
    cd trello-analyzer
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

To use this application, you need to configure your Trello and OpenAI API keys.

#### Getting Your Trello API Key and Token

1. **Trello API Key:**
   - Go to the [Trello API Key page](https://trello.com/app-key). (now there are Power-ups! Follow the instructions)
   - Log in with your Trello account.
   - Copy the API key provided.

2. **Trello Token:**
   - On the same page, click the "Token" link. (It is no the 'Secret', you have to generate a Token, check Trello docs)
   - Authorize the application to access your Trello account.
   - Copy the token provided.

3. **Trello Board ID:**
   - Open your Trello board.
   - The Board ID is part of the URL after `/b/` and before the board name. For example, in the URL `https://trello.com/b/abc12345/my-board`, `abc12345` is the Board ID.

#### Setting Up Your Environment

You can now enter your API keys and Board ID directly through the Streamlit interface:

1. Start the Streamlit application:

    ```bash
    streamlit run main.py
    ```

2. Open your browser and navigate to the URL provided by Streamlit.

3. Enter your Trello API Key, Trello Token, OpenAI API Key, and Trello Board ID in the sidebar and click the save buttons to store them in the `.env` file.

## Running the Application

Once you have configured your API keys and Board ID, you can start analyzing your Trello board.

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the developers of Streamlit, CrewAI, and all the libraries used in this project.
- Special thanks to the Trello team for providing an excellent API.

Enjoy analyzing your Trello boards with the power of multi-agent systems! 🚀