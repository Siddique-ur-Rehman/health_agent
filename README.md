# Health Agent

A simple AI health assistant built with the OpenAI Agents SDK and Google Gemini.

## Features

- General health information
- BMI calculation
- Symptom logging
- Conversation memory using SQLite
- Google Gemini integration
- Tool calling with OpenAI Agents SDK

## Technologies

- Python
- OpenAI Agents SDK
- Google Gemini
- SQLite
- uv
- python-dotenv

## Project Structure

```text
health-agent/
├── health_agents/
│   ├── __init__.py
│   └── health_agent.py
│
├── tools/
│   ├── __init__.py
│   └── health_tools.py
│
├── memory/
│   ├── __init__.py
│   └── session.py
│
├── .env
├── .gitignore
├── main.py
├── pyproject.toml
└── uv.lock
 ```

## Setup

Clone the repository:

git clone https://github.com/Siddique-ur-Rehman/health_agent.git

cd health_agent

Install dependencies:

uv sync

Create a `.env` file:

GEMINI_API_KEY=your_gemini_api_key

## Run

uv run main.py

The agent will run in the terminal and you can interact with it by entering health-related questions.

Type `exit` to stop the application.

## Note

This project is created for learning and general health information purposes. It is not a replacement for professional medical advice or diagnosis.
