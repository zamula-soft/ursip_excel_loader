import os

from db.table_classes import TableTypes
from config.constants import TOTAL_TABLES
from config.mappings import get_total_mapping
from db.sqltables_factory import SQLTablesCreate, SQLTablesUpdate


class SQLiteLoader:
    """
    Load data into app with  models dataclasses
    """

    def __init__(self, conn):
        self.conn = conn

    def load_data(self, row: list):
        """
        Load and update data in DB
        :param row: list
        :return: None
        """
        SQLTablesCreate(self.conn)
        SQLTablesUpdate(self.conn, row)


class SQLTotalResults:
    def __init__(self, conn):
        self.conn = conn

    def get_totals_from_table(self):
        """get totals from DB"""
        dict_result = {}
        for table in TOTAL_TABLES:
            table_func = TableTypes(table)
            row_totals = get_total_mapping[table_func](self.conn)
            for row_total in row_totals:
                totals = list(row_total)
                date_entry = totals.pop()
                dict_result[table, date_entry] = totals
        return dict_result
