import sqlite3
from sqlite3 import Connection, Error


class SQL_DB:
    def init_db(self, db_file):
        """
        Initialize and return a connection to the SQLite database.
        If the database file does not exist, it will be created.
        """
        conn = sqlite3.connect(db_file)
        return conn

    def create_table(self, conn, create_table_sql):
        """
        Create a table using the provided SQL statement.

        Parameters:
        - conn: SQLite connection object
        - create_table_sql: a CREATE TABLE SQL statement string
        """
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()

    def insert_data(self, conn, insert_sql, data_tuple):
        """
        Insert data into a table.

        Parameters:
        - conn: SQLite connection object
        - insert_sql: SQL INSERT statement with placeholders
        - data_tuple: tuple of values to insert
        """
        cursor = conn.cursor()
        cursor.execute(insert_sql, data_tuple)
        conn.commit()

    def query_data(self, conn, query_sql, params=()):
        """
        Query data from the database.

        Parameters:
        - conn: SQLite connection object
        - query_sql: SQL SELECT query string with optional placeholders
        - params: tuple of parameters for the query (default empty)

        Returns:
        - List of tuples with the query results
        """
        cursor = conn.cursor()
        cursor.execute(query_sql, params)
        return cursor.fetchall()

    def close_db(self, conn):
        """
        Close the SQLite database connection.
        """
        if conn:
            conn.close()

    def connect_db(self, db_path) -> Connection:
        """
        Create and return a connection to the SQLite database.
        If the database file does not exist, it will be created.

        Parameters:
        - db_path: path to the SQLite database file (default: url_shortener.db)

        Returns:
        - sqlite3.Connection object
        """
        try:
            conn = sqlite3.connect(db_path)
            # Enable foreign key constraint support
            conn.execute("PRAGMA foreign_keys = ON;")
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None
