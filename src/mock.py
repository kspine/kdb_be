"""Query last record,
all datatype
all template of current user
all shop list
all book list
"""

# T_CONST_DATATYPE
datatype_list = [
    {'id':'测试', 'text':'测试'},
    {'id':'售价', 'text':'售价'},
    {'id':'折扣', 'text':'折扣'},
    {'id':'销量', 'text':'销量'},
    {'id':'评论数', 'text':'评论数'},
    {'id':'直通车投入', 'text':'直通车投入'}
]

# 没有单独的book_list
book_list = [
    {
        'id': '测试',
        'text': '测试'
    },
    {
        'id': '软件工程',
        'text': '软件工程'
    },
    {
        'id': '操作系统',
        'text': '操作系统'
    },
    {
        'id': '计算机网络',
        'text': '计算机网络'
    }
]

book_list2 = [
    {
        'id': '测试',
        'text': '测试'
    },
]

shop_book_list = [
    {'id':'测试', 'text':'测试', 'data': book_list},
    {'id':'人邮', 'text':'人邮', 'data': book_list2},
#    {'id':'新华', 'text':'新华', 'data': book_list},
#    {'id': '当当', 'text': '当当网', 'data': book_list}
]


data = {
    'type': '销量',
    'data': [
        # 一个宫格, 某店某书某指标的走势图
        {
            'shop': {'id': '人邮', 'text':'人邮'},
            'book': {'id': 'python', 'text': 'python'},
            'date': ['2017/06/10', '2017/06/11', '2017/06/12', '2017/06/13', '2017/06/14', ],
            'value': [8, 3, 9, 8, 3, 9],
        },
        {
            'shop': {'id': '人邮', 'text':'人邮'},
            'book': {'id': 'c++', 'text': 'c++'},
            'date': ['2017/06/11', '2017/06/12', '2017/06/13', '2017/06/14', '2017/06/15', ],
            'value': [8, 3, 9, 8, 3, 9],
        }
    ]
}

data_query = {
    'type': '销量',
    'data': [
        # 一个宫格, 某店某书某指标的走势图
        {
            'shop': {'id': '人邮', 'text':'人邮'},
            'book': {'id': 'python', 'text': 'python'},
            'date': ['2017/06/10', '2017/06/11', '2017/06/12', '2017/06/13', '2017/06/14', ],
            'value': [8, 3, 9, 8, 3, 9],
        },
    ]
}

query = {
    'type': '',
    'data': [
        {
            'shop': {'id': '', 'text': '人邮'},
            'book': {'id': '软件工程', 'text': '软件工程'}
        },
        {
            'shop': {'id': '', 'text': '人邮'},
            'book': {'id': '软件工程', 'text': '软件工程'}
        }
    ]
}

templ_list = [
    {
        'id': '123',
        'text': '张三-软件工程-销量',
        #'type': '销量',
        'data': [
            {
                'shop': {'id': '', 'text': '人邮'},
                'book': {'id': '软件工程', 'text': '软件工程'}
            }
        ]
    },
    {
        'id': '456',
        'text': '李四-软件工程-销量',
        #'type': '销量',
        'data': [
            {
                'shop': {'id': '', 'text': '人邮'},
                'book': {'id': '软件工程', 'text': '软件工程'}
            }
        ]
    }
]

init = {
    'data': data,
    'datatype_list': datatype_list,
    'template_list': templ_list,
    'shop_book_list': shop_book_list, # 包含书目
    #'book_list': book_list, # 从 data 中取
}

save_templ = {
    'text': '李四-软件工程-销量',
    #'type': '销量',
    'data': [
        {
            'shop': {'id': '', 'text':'人邮'},
            'book': {'id': '软件工程', 'text': '软件工程'}
        }
    ]
}
