# author: Hendrik Werner // s4549775
# author: Constantin Blach // s4329872

import xlrd
from pylab import *

with xlrd.open_workbook(filename="nanonose.xls") as book:
    # assignment 1.2.1 a
    sheet = book.sheet_by_index(0)
    offset_row = 2
    offset_col = 3
    data = empty((90, 8))
    for row in range(90):
        data[row] = sheet.row_values(rowx=offset_row + row, start_colx=offset_col)
    print(data)

    # assignment 1.2.1 b
    data_plot = scatter(data[:, 0], data[:, 1])
    show()

    # assignment 1.2.2 c
    means = array([data[:, col].mean() for col in range(8)])
    Y = data - np.ones((90, 1)) * means
    U, s, Vt = linalg.svd(Y)
    sum_of_squares = sum([elem ** 2 for elem in s])
    pms = [(s[m] ** 2)/ sum_of_squares for m in range(8)]
    print("Pricipal Components = {}".format(s))
    print("The first 3 PCs account for {}% of variation.".format(sum(pms[:3]) * 100))

    plot(pms)
    show()
