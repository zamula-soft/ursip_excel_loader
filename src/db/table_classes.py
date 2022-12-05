import enum
from abc import ABCMeta, abstractmethod

from db.queries import *
from models.db_models import CompanyData, Fact, Forecast


class TableTypes(str, enum.Enum):
    """Table types"""

    COMPANY_TABLE = 'company_data'
    FACT_TABLE = 'fact'
    FORECAST_TABLE = 'forecast'


class Tables:
    def __init__(self, conn):
        self.conn = conn

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def update_table(self, row):
        pass

    @abstractmethod
    def get_totals(self):
        pass


class TableCompanyData(Tables):
    def create_table(self):
        create_table_company_data(self.conn)

    def update_table(self, row: CompanyData):
        update_company_data(self.conn, row)

    def get_totals(self):
        pass


class TableFact(Tables):
    def create_table(self):
        create_table_fact(self.conn)

    def update_table(self, row: Fact):
        update_fact(self.conn, row)

    def get_totals(self):
        get_total_fact(self.conn)


class TableForecast(Tables):
    def create_table(self):
        create_table_forecast(self.conn)

    def update_table(self, row: Forecast):
        update_forecast(self.conn, row)

    def get_totals(self):
        get_total_forecast(self.conn)