"""Query last record,
all datatype
all template of current user
all shop list
all book list
"""

datatype_list = ['测试', '售价', '折扣', '销量', '评论数', '直通车投入']
shop_list = ['测试', '人民邮电出版社官方旗舰店', '新华文轩', '当当网']
book_list = [
    {
        'isbn': '',
        'name': '测试'
    },
    {
        'isbn': '',
        'name': '软件工程'
    },
    {
        'isbn': '',
        'name': '操作系统'
    },
    {
        'isbn': '',
        'name': '计算机网络'
    }
]


mb = {
    'type': '销量',
    'data': [
        # 一个宫格, 某店某书某指标的走势图
        {
            'shop': '人邮',
            'isbn': '12345678',
            'book': 'python',
            'date': ['2017/06/10', '2017/06/11', '2017/06/12', '2017/06/13', '2017/06/14', ],
            'val': [8, 3, 9, 8, 3, 9],
        },
        {
            'shop': '人邮',
            'isbn': '12345678',
            'book': 'c++',
            'date': ['2017/06/11', '2017/06/12', '2017/06/13', '2017/06/14', '2017/06/15', ],
            'val': [8, 3, 9, 8, 3, 9],
        }
    ]
}

query = {
    'type': '',
    'data': [
        {
            'shop': '',
            'isbn': '',
            'book': '',
        }
        ,
        {
            'shop': '',
            'isbn': '',
            'book': '',
        }
    ]
}

templ_list = [
    {
        'name': '张三-软件工程-销量',
        'type': '销量',
        'data': [
            {
                'shop': '人邮',
                'isbn': '12345678',
                'book': '软件工程'
            }
        ]
    },
    {
        'name': '李四-软件工程-销量',
        'type': '销量',
        'data': [
            {
                'shop': '当当网',
                'isbn': '12345678',
                'book': '操作系统'
            }
        ]
    }
]

init = {
    'm_shop_book_data': mb,
    'datatype_list': datatype_list,
    'template_list': templ_list,
    'shop_list': shop_list,
    'book_list': book_list,
}

save_templ = {
    'name': '李四-软件工程-销量',
    'type': '销量',
    'data': [
        {
            'shop': '人邮',
            'isbn': '12345678',
            'book': '软件工程'
        }
    ]
}
