import csv

import xlrd
from xlsxwriter.workbook import Workbook

from src.another_mod import _private_sub
from src.another_mod import main


def calling():
    print(_private_sub())
    print(main())


def read_numeric_cell_from_excel():
    workbook = xlrd.open_workbook(r'C:\Users\atishayshukla\Desktop\test.xlsx')
    sh = workbook.sheet_by_name('helios')
    for i in range(sh.nrows):
        val = sh.row_values(i)
        with open(r'C:\Users\atishayshukla\Desktop\test.csv', 'a', newline='') as result_file:
            wr = csv.writer(result_file)
            wr.writerow(val)


def csv_to_excel():
    csvfile = r'C:\Users\atishayshukla\Desktop\test.csv'
    xl_file = r'C:\Users\atishayshukla\Desktop\dummy.xlsx'
    workbook = Workbook(xl_file)
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()


if __name__ == '__main__':
    csv_to_excel()
