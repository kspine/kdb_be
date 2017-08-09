0. 公用
    api: api/query_book_list
    in:
    {}
    out:
    ```
    [
        {
            'book': '',
            'name': ''
        },
        {
        }
    ]
    ```
    api: api/query_shop_list

    in:
    {}
    out:
    ```
    [
        {
            'book': '',
            'name': ''
        },
        {
        }
    ]
    ```
    api: api/query_shopbook_list
    in:
    {}
    out:
    ```
    [
        {
            'shop': '',
            'name': '',
            'book_list': [
                {
                    'book': '',
                    'name': ''
                },
                {}
            ]
        },
        {}
    ]
    ```
    api: api/query_temp_list
    in:
    {}
    out:
    ```
    [
    {
        'id': '123',
        'name': '张三-软件工程-销量',
        #'type': '销量',
        'shopbook_list': [
            {'shop': '', 'shop_name': '人邮', 'book': '', 'book_name': ''},
            {}
        ]
    },
    {
        'id': '456',
        'name': '李四-软件工程-销量',
        #'type': '销量',
        'data': [
            {
                'shop': {'id': '', 'text': '人邮'},
                'book': {'id': '软件工程', 'text': '软件工程'}
            }
        ]
    }
]
    ```
    api: api/query_datatype_list
    in:
    {}
    out:
    ```
    [
        {'id':'测试', 'text':'测试'},
        {'id':'售价', 'text':'售价'},
        {'id':'折扣', 'text':'折扣'},
        {'id':'销量', 'text':'销量'},
        {'id':'评论数', 'text':'评论数'},
        {'id':'直通车投入', 'text':'直通车投入'}
    ]
    ```

1. 单品初始化
   api: api/query_book_mshop_init_data
   in:
   {}

   out:
   ```
   [
        {'id': '', 'text': ''},
   ]
   ```


1. 单品销售情况查询
   api: /api/query_book_mshop_data
   in: ISBN 日期
   {
    'book': {'id': '', 'text': ''},
    'period': {}
    }
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

   查询宫格内容

   api: /api/query_mshopbook_data
   in:
   ```
{'type': 'price', 'data': [{'book': {'text': 'Python参考手册(第4版·修订版)', 'id': '9787115394392'}, 'shop': {'text': '人民邮电出版社官方旗舰店', 'id': 'rmydcbs'}}, {'book': {'text': 'Python高性能编程', 'id': '9787115454898'}, 'shop': {'text': '新华文轩网络书店', 'id': 'winshare'}}]}
```
    out:

  
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
