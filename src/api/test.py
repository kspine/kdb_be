#-*- coding: utf-8 -*-

# sync
param_sync_exp_schema = [
                    {
                        "name":"KYLIN",
                        "object":[
                            {
                                "checked":True, # 后台没有使用
                                "name":"TEST",
                                "clause":""
                                }
                            ]
                        }
                    ]

param_sync_imp_schema = [] #导入指定表

# 接口参数
param_db_src = {
        "db_type": "oracle",
        "db_ip": "172.16.1.199",
        "db_port": 1521,
        "db_user": "kylin",
        "db_password": "oracle",
        "db_id": "orcl",
        "as_source_db": "yes",
        "db_name":"rkw"
        }

param_db_dst = {
        "db_type": "oracle",
        "db_ip": "172.16.1.199",
        "db_port": 1521,
        "db_user": "kylin",
        "db_password": "oracle",
        "db_id": "orcl",
        "as_source_db": "no",
        "db_name":"rkw"
        }

# 根据loader配置信息生成
# param_capture_filter = ['KYLIN']

param_loader_filter = [
                    {
                        "filter_type": "INCLUDE",
                        "schema": [
                            {
                                "name": "KYLIN",
                                "mapping_name": "KYLIND",
                                "object_type": [
                                    {
                                        "name": "TABLE",
                                        "object": [
                                            {
                                                "name": "TEST02"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                    {
                        "filter_type": "EXCLUDE",
                        "schema": []
                        }
                    ]
_param_loader_filter = [
                    {
                        "filter_type": "INCLUDE",
                        "schema": [
                            {
                                "name": "KYLIND",
                                "mapping_name": "KYLIN",
                                "object_type": [
                                    {
                                        "name": "TABLE",
                                        "object": [
                                            {
                                                "name": "TEST"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                    {
                        "filter_type": "EXCLUDE",
                        "schema": []
                        }
                    ]

param_loader_filter12 = [
                    {
                        "filter_type": "INCLUDE",
                        "schema": [
                            {
                                "name": "KYLIND",
                                "mapping_name": "KYLIN",
                                "object_type": [
                                    {
                                        "name": "TABLE",
                                        "object": [
                                            {
                                                "name": "TEST"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                "name": "KYLIN_X01",
                                "mapping_name": "KYLIND_X01",
                                "object_type": [
                                    {
                                        "name": "TABLE",
                                        "object": [
                                            {
                                                "name": "TEST02"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                    {
                        "filter_type": "EXCLUDE",
                        "schema": []
                        }
                    ]

param_start_plus = {
        "param_db_src": param_db_src,
        "param_db_dst": param_db_dst,
        "param_loader_filter": param_loader_filter
        }

response = {
    "group_id": "group_01"
}

param_stop_plus = {
        "group_id": "group_id"
        }

response = {
    "result": True
}

param_query_status = {
        "group_id": "group_id"
}

response = {"server":[
    {
        "name":"capture_4",
        "type":"capture",
        "thread":"0",
        "status":"running",
        "start_time":"2017-05-17 14:37:10",
        "work_scn":"5588165",
        "work_scn_time":"2017-05-17 14:47:16",
        "errmsg":"",
        "op_insert":"0",
        "op_update":"0",
        "op_delete":"0",
        "op_ddl":"1"
    },
    {
        "name":"apply_5",
        "type":"apply",
        "thread":"0",
        "status":"running",
        "start_time":"2017-05-17 14:37:19",
        "work_scn":"5588165",
        "work_scn_time":"2017-05-17 14:47:16",
        "errmsg":"",
        "op_insert":"0",
        "op_update":"0",
        "op_delete":"0",
        "op_ddl":"1"
    }
]}

param_start_plus2 = {"param_db_src":{"db_type":"oracle","db_ip":"172.16.1.62","db_port":"1521","db_user":"zdg_test_dcp1","db_password":"123456","db_id":"orcl","as_source_db":"yes","db_name":"orcl"},"param_db_dst":{"db_type":"oracle","db_ip":"172.16.1.178","db_port":"1521","db_user":"zdg_test_dcp1","db_password":"123456","db_id":"orcl","as_source_db":"no","db_name":"orcl"},"param_loader_filter":[{"filter_type":"INCLUDE","schema":[{"name":"ZDG_TEST_DCP1","mapping_name":"ZDG_TEST_DCP1","object_type":[{"name":"TABLE","object":[{"name":"DATATYPE_1","mapping_name":"DATATYPE_1"}]}]}]},{"filter_type":"EXCLUDE","schema":[]}]}

# 错误返回
{
    "request" : "/dipserver/start_plus",
    "error_code" : "10105",
    "error" : "forbidden"
}

if __name__ == '__main__':
    schemas = gen_capture_filter(param_loader_filter)
    print(schemas)
