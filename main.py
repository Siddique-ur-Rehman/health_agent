import asyncio

from agents import Runner

from health_agents.health_agent import health_agent
from memory.session import create_session


async def main():

    print("Health Agent")
    print("Type 'exit' to quit.\n")

    session = create_session("user_001")

    while True:

        user_input = input("You: ")

        if user_input.lower().strip() == "exit":
            break

        result = await Runner.run(
            health_agent,
            user_input,
            session=session,
        )

        print(f"\nAgent: {result.final_output}\n")


if __name__ == "__main__":
    asyncio.run(main())