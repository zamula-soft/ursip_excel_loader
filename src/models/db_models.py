import enum
from dataclasses import dataclass, field


@dataclass
class CompanyData:
    id: int
    company: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Fact:
    company_id: int
    fact_qlib_data1: int
    fact_qlib_data2: int
    fact_qoil_data1: int
    fact_qoil_data2: int

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Forecast:
    company_id: int
    forecast_qlib_data1: int
    forecast_qlib_data2: int
    forecast_qoil_data1: int
    forecast_qoil_data2: int

    def __getitem__(self, item):
        return getattr(self, item)


class TableTypes(str, enum.Enum):
    """Table types"""

    COMPANY_TABLE = 'company_data'
    FACT_TABLE = 'fact'
    FORECAST_TABLE = 'forecast'