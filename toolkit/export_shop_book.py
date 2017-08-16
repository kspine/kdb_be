#encoding:utf-8       #设置编码方式

import xlwt
wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)  ##第二参数用于确认同一个cell单元是否可以重设值。

row = 0
cols = ["shop", "shop_name", "book", "book_name", "shopbook_url"]
for i, col in enumerate(cols):
    sheet.write(row, i, col)

style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
style.font = font
sheet.write(0, 1, 'some bold Times text', style)

wbk.save('/kdb/TestData2.xls')    ##该文件名必须存在
