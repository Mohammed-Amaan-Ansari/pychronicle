from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATABASE_PATH = PROJECT_ROOT / "pychronicle.db"


def get_connection():
    """
    Returns a SQLite connection.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    return connection

from pychronicle.storage.models import VariableState


def insert_variable_state(state: VariableState):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO variable_history
        (
            timestamp,
            line_number,
            variable_name,
            serialized_value
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            state.timestamp,
            state.line_number,
            state.variable_name,
            state.serialized_value,
        ),
    )

    connection.commit()

    connection.close()

def get_all_variable_states():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            timestamp,
            line_number,
            variable_name,
            serialized_value
        FROM variable_history
        ORDER BY id
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows