import os

from models.db_models import TableTypes
from config.constants import TABLES, TOTAL_TABLES
from config.mappings import create_table_mapping, get_data_from_row_mapping, update_data_mapping, get_total_mapping


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
        self.init_db()
        self.update_data_in_tables(row)

    def init_db(self):
        """Connect or create and connect to DB"""
        for table in TABLES:
            table_func = TableTypes(table)
            create_table_mapping[table_func](self.conn)

    def update_data_in_tables(self, row: list):
        """Update data in tables"""
        for table in TABLES:
            table_func = TableTypes(table)
            data_kwargs = get_data_from_row_mapping[table_func](row)
            update_data_mapping[table_func](self.conn, data_kwargs)

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
