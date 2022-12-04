from models.db_models import TableTypes

from app.extract_utils import *
from db.queries import *


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
    TableTypes.COMPANY_TABLE: create_update_company_data,
    TableTypes.FACT_TABLE: create_update_fact,
    TableTypes.FORECAST_TABLE: create_update_forecast,
}

get_total_mapping = {
    TableTypes.FACT_TABLE: get_total_fact,
    TableTypes.FORECAST_TABLE: get_total_forecast,
}