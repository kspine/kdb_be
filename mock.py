"""Query last record,
all datatype
all template of current user
all shop list
all book list
"""

datatype_list = [
    {'id':'测试', 'text':'测试'},
    {'id':'售价', 'text':'售价'},
    {'id':'折扣', 'text':'折扣'},
    {'id':'销量', 'text':'销量'},
    {'id':'评论数', 'text':'评论数'},
    {'id':'直通车投入', 'text':'直通车投入'}
]

shop_list = [
    {'id':'测试', 'text':'测试'},
    {'id':'测试', 'text':'测试'},
    {'id':'人邮', 'text':'人邮'},
    {'id':'新华', 'text':'新华'},
    {'id': '当当', 'text': '当当网'}
]

# 没有单独的book_list
book_list = [
    {
        'id': '',
        'text': '测试'
    },
    {
        'id': '',
        'text': '软件工程'
    },
    {
        'id': '',
        'text': '操作系统'
    },
    {
        'id': '',
        'text': '计算机网络'
    }
]


data = {
    'type': '销量',
    'data': [
        # 一个宫格, 某店某书某指标的走势图
        {
            'shop': {'id': '人邮', 'text':'人邮'},
            'book': {'id': 'python', 'text': 'python'},
            'date': ['2017/06/10', '2017/06/11', '2017/06/12', '2017/06/13', '2017/06/14', ],
            'val': [8, 3, 9, 8, 3, 9],
        },
        {
            'shop': {'id': '人邮', 'text':'人邮'},
            'book': {'id': 'c++', 'text': 'c++'},
            'date': ['2017/06/11', '2017/06/12', '2017/06/13', '2017/06/14', '2017/06/15', ],
            'val': [8, 3, 9, 8, 3, 9],
        }
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
        'id': '',
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
        'id': '',
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
    'shop_list': shop_list,
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
