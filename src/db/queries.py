from models.db_models import CompanyData, Fact, Forecast


def create_table_company_data(conn):
    """
    create if not exist table company_data
    :param conn:
    :return:
    """
    cursor = conn.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS company_data(id INTEGER PRIMARY KEY,  company NVARCHAR NOT NULL);'
    cursor.execute(sql)
    conn.commit()


def create_table_fact(conn):
    """
    create if not exist table company_data
    :param cursor:
    :param conn:
    :return:
    """
    cursor = conn.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS fact(company_id INTEGER PRIMARY KEY,  fact_qlib_data1 INTEGER NOT NULL, ' \
          'fact_qlib_data2 INTEGER NOT NULL, ' \
          'fact_qoil_data1 INTEGER NOT NULL, ' \
          'fact_qoil_data2 INTEGER NOT NULL,' \
          'date_entry DATE);'
    cursor.execute(sql)
    conn.commit()


def create_table_forecast(conn):
    """
    create if not exist table company_data
    :param cursor:
    :param conn:
    :return:
    """
    cursor = conn.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS forecast(' \
          'company_id INTEGER PRIMARY KEY,  ' \
          'forecast_qlib_data1 INTEGER NOT NULL, ' \
          'forecast_qlib_data2 INTEGER NOT NULL, ' \
          'forecast_qoil_data1 INTEGER NOT NULL, ' \
          'forecast_qoil_data2 INTEGER NOT NULL, ' \
          'date_entry DATE);'
    cursor.execute(sql)
    conn.commit()


def create_update_company_data(conn, row: CompanyData):
    """
    :param conn:
    :param row: CompanyData
    :return: None
    """
    cursor = conn.cursor()
    sql = f"INSERT INTO company_data (id, company) " \
          f"VALUES ({row['id']}, '{row['company']}')" \
          f"ON CONFLICT (id) DO NOTHING;"
    cursor.executescript(sql)
    conn.commit()


def create_update_fact(conn, row: Fact):
    """
    :param conn:
    :param row: Fact
    :return: None
    """
    cursor = conn.cursor()
    sql = f"INSERT INTO fact (company_id, fact_qlib_data1, fact_qlib_data2," \
          f" fact_qoil_data1, fact_qoil_data2, date_entry)" \
          f" VALUES ({row['company_id']}, " \
          f" {row['fact_qlib_data1']}, {row['fact_qlib_data2']}," \
          f" {row['fact_qoil_data1']}, {row['fact_qoil_data2']}, " \
          f" {row['date_entry']})" \
          f" ON CONFLICT (company_id) DO UPDATE SET " \
          f"fact_qlib_data1={row['fact_qlib_data1']}, " \
          f"fact_qlib_data2={row['fact_qlib_data2']}, " \
          f"fact_qoil_data1={row['fact_qoil_data1']}, " \
          f"fact_qoil_data2={row['fact_qoil_data2']}, " \
          f"date_entry={row['date_entry']}" \
          f";"
    cursor.executescript(sql)
    conn.commit()


def create_update_forecast(conn, row: Fact):
    """
    :param row: Forecast
    :return: None
    """
    cursor = conn.cursor()
    sql = f"INSERT INTO forecast (company_id, forecast_qlib_data1, forecast_qlib_data2, forecast_qoil_data1, " \
          f"forecast_qoil_data2, date_entry) " \
          f"VALUES ({row['company_id']}, {row['forecast_qlib_data1']}, {row['forecast_qlib_data2']}," \
          f" {row['forecast_qoil_data1']}, {row['forecast_qoil_data2']}, {row['date_entry']})" \
          f" ON CONFLICT (company_id) DO UPDATE SET " \
          f"forecast_qlib_data1={row['forecast_qlib_data1']}, " \
          f"forecast_qlib_data2={row['forecast_qlib_data2']}, " \
          f"forecast_qoil_data1={row['forecast_qoil_data1']}, " \
          f"forecast_qoil_data2={row['forecast_qoil_data2']},  " \
          f"date_entry={row['date_entry']}" \
          f";"
    cursor.executescript(sql)
    conn.commit()


def get_total_fact(conn):
    """
    get all totals from fact
    :param conn:
    :return:
    """
    cursor = conn.cursor()
    sql = 'SELECT SUM(f.fact_qlib_data1), ' \
          'SUM(f.fact_qlib_data2), ' \
          'SUM(f.fact_qlib_data1), ' \
          'SUM(f.fact_qlib_data1), '\
          'f.date_entry '\
          'FROM fact f ' \
          'JOIN company_data c ON c.id = f.company_id GROUP BY company, f.date_entry;'
    cursor.execute(sql)
    row = cursor.fetchall()
    conn.commit()
    return row


def get_total_forecast(conn):
    """
    get all totals from fact
    :param conn:
    :return:
    """
    cursor = conn.cursor()
    sql = 'SELECT SUM(f.forecast_qlib_data1), ' \
          'SUM(f.forecast_qlib_data2),' \
          'SUM(f.forecast_qlib_data1),' \
          'SUM(f.forecast_qlib_data1),' \
          'f.date_entry ' \
          'FROM forecast f ' \
          'JOIN company_data c ' \
          'ON c.id = f.company_id GROUP BY company, f.date_entry;'
    cursor.execute(sql)
    row = cursor.fetchall()
    conn.commit()
    return row
