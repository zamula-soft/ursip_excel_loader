import os
import sqlite3
from dotenv import load_dotenv
from contextlib import contextmanager

from config.constants import EXCEL_FILEPATH
from app.extract_data import ExcelData
from app.load_data import SQLiteLoader, SQLTotalResults


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.commit()
    conn.close()


def load_into_sqlite(sqlite_conn: sqlite3.Connection, data: list):
    """Load Excel data into SQLite"""
    sqlite_loader = SQLiteLoader(sqlite_conn)
    for row in data:
        sqlite_loader.load_data(row)


def get_total_dict_results(sqlite_conn: sqlite3.Connection):
    sqlite_results = SQLTotalResults(sqlite_conn)
    total_dict_results = sqlite_results.get_totals_from_table()
    print(total_dict_results)


if __name__ == '__main__':
    load_dotenv()

    excel_data = ExcelData(EXCEL_FILEPATH)
    data = excel_data.extract_data()
    db_path = os.environ.get('SQLT_DBNAME')
    with conn_context(db_path) as sqlite_conn:
        load_into_sqlite(sqlite_conn, data)
        get_total_dict_results(sqlite_conn)
