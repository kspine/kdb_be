#-*- encoding:utf-8 -*-

import xlrd
import sqlite3

conn = sqlite3.connect('/kdb/kdb1.sqlite')

xlsx = '/kdb/shopbook.xlsx'
workbook = xlrd.open_workbook(xlsx)
print ("There are {} sheets in the workbook".format(workbook.nsheets))

shop_list = []
book_list = []
shopbook_list = []

cols = ["shop", "shop_name", "book", "book_name", "shopbook_url"]
booksheet = workbook.sheet_by_index(0)
for row in range(booksheet.nrows):
    if row == 0:
        continue
    shop = (booksheet.cell(row, 0).value, booksheet.cell(row, 1).value)
    if shop not in shop_list:
        shop_list.append(shop)
    book = (booksheet.cell(row, 2).value, booksheet.cell(row, 3).value)
    if book not in book_list:
        book_list.append(book)
    shopbook = (booksheet.cell(row, 0).value, booksheet.cell(row, 2).value, booksheet.cell(row, 4).value)
    if shopbook not in shopbook_list:
        shopbook_list.append(shopbook)

# print(shop_list)
conn.executemany('insert into t_basic_shop (shop, name) values (?, ?)', shop_list)
# print(book_list)
conn.executemany('insert into t_basic_book (book, name) values (?, ?)', book_list)
# print(shopbook_list)
conn.executemany('insert into t_basic_shopbook (shop, book, url) values (?, ?, ?)', shopbook_list)
conn.commit()
