import os
from openpyxl import load_workbook


class ExcelData:
    def __init__(self, filepath):
        self.filepath = filepath

    def extract_data(self):
        wb = load_workbook(self.filepath)
        ws = wb[wb.sheetnames[0]]
        data = list(ws.rows)[3:]

        return data
