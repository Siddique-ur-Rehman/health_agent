from agents import SQLiteSession


def create_session(session_id: str) -> SQLiteSession:
    """
    Create a persistent SQLite conversation session.
    """

    return SQLiteSession(
        session_id,
        "health_agent_memory.db",
    )
