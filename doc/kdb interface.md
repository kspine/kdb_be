1. 单品销售情况查询
   api: api/query_book_mdata
   in: ISBN 日期
   > 日期, 具体某一天, 最近一周, 最近一月等

   ```
   {
       isbn:'9787115414779',
       date:['2017-05-03', '2017-06-03']
   }
   ```
   > date, 如果数组只有一个元素, 表示具体某一天<br>
     如果有两个元素, 则分别表示起止日期<br>
     否则按错误入参处理

   out:

   ```
   [
       {
           'shop':'',
           'price':'',
           'discount':'',
           'sale':'',
           'flow':'',
           'comment':'',
           'ztc':''
       },
       {

       }
   ]
   ```

2. 竞品情况比较
   api: api/query_shopbook_data
   in: N*店铺_ISBN + 数据项 + 周期

   ```
   {
       'shop_isbn':[''],
       'datatype':'',
       'duration':''
   }
   ```

   out:

   ```
   [
       //一个宫格
       {
           'shop':'',
           'data':[
                //一个 (x,y)
                {
                   'date':'',
                   'val':''
                },
                {

                }
            ]
       },
       ,
       {

       }
   ]
   ```
  
3. 某类目特殊表现监
   api: api/query_concerned_data
   in:

   ```
   {
       'function_id':''
       'duration':[]
   }
   ```

   out:

   ```
   [
       //一个公式
       {
           'function_id'='',
           'result':[
               {
                  'shop_book':'',
                  'val':''
                  'date':''
               },
               {

               }
           ],
       }
       {

       }
   ]
   ```