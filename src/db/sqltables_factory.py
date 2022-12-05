import os

from db.table_classes import TableTypes
from config.constants import TABLES
from config.mappings import table_classes_dict, create_table_mapping, get_data_from_row_mapping, update_data_mapping


class SQLTablesCreate:
    def __init__(self, conn):
        """Connect or create and connect to DB"""
        self.conn = conn
        for table in TABLES:
            table_func = TableTypes(table)
            table_class = table_classes_dict[table_func](self.conn)
            table_class.create_table()


class SQLTablesUpdate:
    def __init__(self, conn, row: list):
        """Update data in tables"""
        self.conn = conn
        for table in TABLES:
            table_func = TableTypes(table)
            data_kwargs = get_data_from_row_mapping[table_func](row)
            table_class = table_classes_dict[table_func](self.conn)
            table_class.update_table(data_kwargs)
