# Mood AI --- Multi-Personality Chatbot

Mood AI is a Python chatbot built with **LangChain** and **Groq**. It
offers three AI personalities---Angry, Funny, and Sad---and includes
both a terminal-based chatbot and a Streamlit web interface.

## Features

-   **Three selectable personalities**
    -   😡 **Angry Mode** --- responds aggressively and impatiently.
    -   😂 **Funny Mode** --- responds with humor and jokes.
    -   😢 **Sad Mode** --- responds in a sorrowful style.
-   **Groq LLM integration** using `openai/gpt-oss-120b`.
-   **Temperature:** `0.9`.
-   **Conversation history** maintained with LangChain message objects.
-   **Streamlit UI** with a custom dark theme and chat-style messages.
-   **Switch personalities** in the Streamlit interface while retaining
    the visible conversation history.
-   Type `0` to exit the terminal chatbot or end the Streamlit
    conversation.

## Tech Stack

-   Python
-   Streamlit
-   LangChain Core
-   LangChain Groq
-   python-dotenv
-   Groq API

## Project Structure

``` text
mood-ai/
├── chatbot.py          # Terminal-based chatbot
├── Chatbot_UI.py       # Streamlit web interface
├── .env                # API key configuration (do not commit)
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

-   Python installed
-   A valid Groq API key
-   Internet access for API requests

## Setup and Installation

### 1. Clone your repository

``` bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your repository URL and folder name.

### 2. Create a virtual environment

**Windows (PowerShell):**

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

``` bat
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the required packages

The project's current `requirements.txt` contains several Generative AI
libraries but does not list Streamlit. Install the packages required by
this chatbot with:

``` bash
python -m pip install streamlit langchain-groq langchain-core python-dotenv
```

Alternatively, add `streamlit` to your `requirements.txt` and install
the project dependencies:

``` bash
python -m pip install -r requirements.txt
```

### 4. Configure the Groq API key

Create a `.env` file in the project root:

``` env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own key. The application uses
`load_dotenv()` to load environment variables.

**Security:** Never commit `.env` to Git or include API keys in source
code, README files, screenshots, or public repositories. If a key has
already been exposed, revoke or rotate it with the provider and update
your local `.env` file.

## Run the Chatbot

### Option A: Streamlit web UI

Run:

``` bash
streamlit run Chatbot_UI.py
```

Open the local URL shown in the terminal (usually
`http://localhost:8501`).

In the UI: 1. Select **Angry Mode**, **Funny Mode**, or **Sad Mode**. 2.
Enter a message in the chat input. 3. Continue the conversation;
messages remain visible during the session. 4. Switch personalities to
change the system prompt. The existing history is retained, and earlier
messages may still influence the model's responses. 5. Enter `0` to end
the conversation.

### Option B: Terminal chatbot

Run:

``` bash
python chatbot.py
```

Choose a mode when prompted: - `1` for Angry Mode - `2` for Funny Mode -
`3` for Sad Mode

Enter messages in the terminal. Type `0` to exit.

## Model Configuration

Both chatbot versions use the following model configuration:

``` python
ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.9
)
```

The system message defines the selected personality. Temperature
influences response variation; it does not guarantee a particular tone.

## Notes and Limitations

-   A valid Groq API key and internet connection are required.
-   Chat history is held in memory during the current terminal process
    or Streamlit session; it is not saved to a database.
-   In the Streamlit version, changing the personality updates the
    system message and preserves the visible conversation. Previous
    messages can still affect the model's response.
-   The terminal script expects a valid mode selection (`1`, `2`, or
    `3`).

## License

No license has been specified. Add a license file if you plan to
distribute the project.
