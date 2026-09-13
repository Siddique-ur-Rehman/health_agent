import os

from dotenv import load_dotenv

from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

from tools.health_tools import (
    calculate_bmi,
    log_symptom,
)


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set in the environment."
    )


# Gemini OpenAI-compatible client
gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


# Gemini model used by the OpenAI Agents SDK
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-3.6-flash",
    openai_client=gemini_client,
)


health_agent = Agent(
    name="Health Assistant",
    instructions="""
You are a general health information assistant.

Your purpose is to provide general health education and
help users organize the health information they provide.

Important safety rules:

1. Do not claim to diagnose diseases.
2. Do not pretend to be a doctor.
3. Do not provide dangerous or overly confident medical advice.
4. When symptoms may indicate an emergency, advise the user
   to seek urgent professional medical care.
5. Ask relevant follow-up questions when necessary.
6. Clearly distinguish general information from professional
   medical diagnosis or treatment.
7. Use the available tools when they are useful.
8. Keep responses understandable and reasonably concise.
""",
    model=gemini_model,

    tools=[
        calculate_bmi,
        log_symptom,
    ],
)


# We are using Gemini rather than OpenAI.
set_tracing_disabled(True)