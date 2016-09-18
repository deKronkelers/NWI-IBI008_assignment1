# author: Hendrik Werner // s4549775
# author: Constantin Blach // s4329872

import xlrd
from pylab import *

# assignment 1.2.1
with xlrd.open_workbook(filename="nanonose.xls") as book:
    sheet = book.sheet_by_index(0)
    offset_row = 2
    offset_col = 3
    data = empty((90, 8))
    for row in range(90):
        data[row] = sheet.row_values(rowx=offset_row + row, start_colx=offset_col)
    print(data)

    # assignment 1.2.2
    data_plot = scatter(data[:, 0], data[:, 1])
    show()
