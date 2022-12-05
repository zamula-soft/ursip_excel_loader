from db.table_classes import TableTypes, Tables, TableCompanyData, TableFact, TableForecast

from app.extract_utils import *
from db.queries import *

table_classes_dict = {
    TableTypes.COMPANY_TABLE: TableCompanyData,
    TableTypes.FACT_TABLE: TableFact,
    TableTypes.FORECAST_TABLE: TableForecast,
}

create_table_mapping = {
    TableTypes.COMPANY_TABLE: create_table_company_data,
    TableTypes.FACT_TABLE: create_table_fact,
    TableTypes.FORECAST_TABLE: create_table_forecast,
}

get_data_from_row_mapping = {
    TableTypes.COMPANY_TABLE: get_from_row_company_data,
    TableTypes.FACT_TABLE: get_from_row_fact,
    TableTypes.FORECAST_TABLE: get_from_row_forecast,
}

update_data_mapping = {
    TableTypes.COMPANY_TABLE: update_company_data,
    TableTypes.FACT_TABLE: update_fact,
    TableTypes.FORECAST_TABLE: update_forecast,
}

get_total_mapping = {
    TableTypes.FACT_TABLE: get_total_fact,
    TableTypes.FORECAST_TABLE: get_total_forecast,
}