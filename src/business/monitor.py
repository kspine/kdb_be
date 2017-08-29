import pandas as pd

from data_model.table import T_Basic_ShopBook
from data_model.table import T_Business_Monitor_Data
from component.formula import Formula
from data_model.db import DbHandler

class Monitor:
    @staticmethod
    def scan():
        # query shopbook
        shopbook_list = T_Basic_ShopBook.query_shopbook_list()
        formula_list = Formula.query_all()
        if not formula_list:
            return

        #sale|avg|5|>|avg|1|10%
        # parse formula

        db_hdl = DbHandler()
        # gen sql
        for f in formula_list:
            formula_id = f[0]
            formula=f[2].split('|')
            datatype = formula[0]
            agg1=formula[1]
            agg1=agg1.replace('avg', 'mean')
            duration1=formula[2]
            op=formula[3]
            agg2=formula[4]
            agg2=agg2.replace('avg', 'mean')
            duration2=formula[5]
            val=formula[6]
            per=True if val.endswith('%') else False
            if per:
                val=val[:-1]

            for i in shopbook_list:
                shop = i[0]
                book = i[1]
                value_his = 0
                value = 0
                _sql = "select value from t_data where shop='{shop}' and book='{book}' and datatype='{datatype}' order by date desc limit {duration}".format(shop=shop, book=book, datatype=datatype, duration=duration1)
                r = db_hdl.query(_sql)
                if not r:
                    continue
                value = r[0][0]

                _sql = "select value from t_data where shop='{shop}' and book='{book}' and datatype='{datatype}' order by date desc limit {duration}".format(shop=shop, book=book, datatype=datatype, duration=duration1)
                # query
                r = db_hdl.query(_sql)
                if not r:
                    continue
                value_his = [i[0] for i in r]
                s_his = pd.Series(value_his)
                if datatype in ['sale', 'comment']:
                    s_his_ = s_his.shift(1)
                    s_his = s_his - s_his_.fillna(0)
                value_his = eval('s_his.{}()'.format(agg1))

                bingo = False
                if per:
                    val = float(val)
                    value = float(value)
                    value_his = float(value_his)
                    if value == 0:
                        continue
                    if eval("100*(value - value_his)/value {op} val".format(op=op)):
                        bingo=True
                else:
                    if eval("value - value_his {op} val".format(op=op)):
                        bingo=True
                if bingo:
                    T_Business_Monitor_Data.add(shop, book, datatype, value, value_his, formula_id)
