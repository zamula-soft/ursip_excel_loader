from config import constants as const
from models.db_models import CompanyData, Fact, Forecast


def get_from_row_company_data(row: list):
    """
    Getting Company_data from row
    :param row: list
    :return: CompanyData
    """
    id = row[const.EXCEL_ID].value
    company = row[const.EXCEL_COMPANY].value
    return CompanyData(id, company)


def get_from_row_fact(row: list):
    """
    Getting Fact from row
    :param row: list
    :return: Fact
    """
    id = row[const.EXCEL_ID].value
    fact_qlib_data1 = row[const.EXCEL_FACT_QLIB_DATA1].value
    fact_qlib_data2 = row[const.EXCEL_FACT_QLIB_DATA2].value
    fact_qoil_data1 = row[const.EXCEL_FACT_QOIL_DATA1].value
    fact_qoil_data2 = row[const.EXCEL_FACT_QOIL_DATA2].value
    return Fact(id, fact_qlib_data1, fact_qlib_data2, fact_qoil_data1, fact_qoil_data2)


def get_from_row_forecast(row: list):
    """
    Getting Fact from row
    :param row: list
    :return: Fact
    """
    id = row[const.EXCEL_ID].value
    forecast_qlib_data1 = row[const.EXCEL_FORECAST_QLIB_DATA1].value
    forecast_qlib_data2 = row[const.EXCEL_FORECAST_QLIB_DATA2].value
    forecast_qoil_data1 = row[const.EXCEL_FORECAST_QOIL_DATA1].value
    forecast_qoil_data2 = row[const.EXCEL_FORECAST_QOIL_DATA2].value
    return Forecast(id, forecast_qlib_data1, forecast_qlib_data2, forecast_qoil_data1, forecast_qoil_data2)
