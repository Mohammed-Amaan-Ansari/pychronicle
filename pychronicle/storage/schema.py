from pychronicle.storage.database import get_connection


CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS variable_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp REAL NOT NULL,

    line_number INTEGER NOT NULL,

    variable_name TEXT NOT NULL,

    serialized_value TEXT NOT NULL

);
"""


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(CREATE_TABLE)

    connection.commit()

    connection.close()