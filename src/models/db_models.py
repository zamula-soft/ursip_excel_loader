import datetime
from dataclasses import dataclass, field


@dataclass
class CompanyData:
    id: int
    company: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Mixin:
    company_id: int
    date_entry: datetime

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Fact(Mixin):
    fact_qlib_data1: int
    fact_qlib_data2: int
    fact_qoil_data1: int
    fact_qoil_data2: int


@dataclass
class Forecast(Mixin):
    forecast_qlib_data1: int
    forecast_qlib_data2: int
    forecast_qoil_data1: int
    forecast_qoil_data2: int

