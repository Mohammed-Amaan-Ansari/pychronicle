from pychronicle.storage.database import get_connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS variable_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp REAL NOT NULL,

        line_number INTEGER NOT NULL,

        variable_name TEXT NOT NULL,

        serialized_value TEXT NOT NULL

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS execution_trace (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp REAL NOT NULL,

        event_type TEXT NOT NULL,

        line_number INTEGER NOT NULL,

        function_name TEXT NOT NULL,

        locals_snapshot TEXT NOT NULL

    )
    """)

    connection.commit()

    connection.close()