# coding:utf-8

from util.alchemy import AlchemyEncoder
from util.alchemy import to_dict
import json

dddddddddddddddddddddddddddd = {
    'ddddddddddddddddddddddddddddddddddddd': 'kkkkk',
    'kkkkkkkkkk': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
}

dddddddddddddddddddddddddddddddddd = {
    'kkklpppppppppppppppppppppppppppppppppppppppppppppp':
    'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',
    'kkkkkkkkkkk': 'd'}


def test_helper():
    from helper.oracle import OracleHelper
    group_id = 'group_36'
    db_id = 'database_135'
    nls = OracleHelper.get_nls_lang(group_id, db_id)

    print(nls)


def test():
    from component.dataflow import Dataflow
    from data_model.db import DbHandler
    from component.component import Db, Capture, Queue, Loader, Sync, T

    t = T()
    t.id = 'etl_6'
    r = t._query_rule('query_etl_delete_config', 'group_1', 'KYLIN', 'TEST')
    r = t._query_rule('query_etl_map_config', 'group_1', 'KYLIN', 'TEST')
    print(r)
    exit(0)

    l = Loader()
    l.remove_table_web([('KYLIND', 'KYLIN', 'TEST', None)])
    exit(0)

    #loader = Loader()
    group_id = 'group_9'
    loader_id = 'apply_37'
    database_id = 'database_33'
    sync_id = 4

    db = Db()
    #r = db.get_curr_scn(group_id, database_id)
    #r = hdl.fetch()
    # print(r)

    #loader.start_with_scn(group_id, loader_id, 1)
    sync = Sync()
    #sync_id = sync.create(group_id, loader_id)
    group_id = 'group_5'
    capture_id = 'capture_11'
    loader_id = 'apply_13'
    sync_id = 5
    scn = 4582717
    #sync.start(group_id, loader_id, sync_id)

    g = Dataflow()
    c = Capture()
    l = Loader()
    q = Queue()
    #c.start(group_id, capture_id)
    #l.start(group_id, loader_id)
    #l.start_with_scn(group_id, loader_id, scn)
    #c.stop(group_id, capture_id)
    #l.stop(group_id, loader_id)
    #r = g.stop(group_id)

    group_id = 'group_5'
    r = g.start(group_id)
    r = g.stop(group_id)
    print(r)
    exit(0)
    queue_id = 'queue_46'
    sdb_id = 'database_41'
    capture_id = 'capture_42'
    ddb_id = 'database_47'
    loader_id = 'apply_48'
    #comp_info = db.get_info(db_id)
    # print(comp_info)

    r = db.delete(group_id, sdb_id)
    print(r)
    r = c.delete(group_id, capture_id)
    print(r)
    r = q.delete(group_id, queue_id)
    print(r)
    r = l.delete(group_id, loader_id)
    print(r)
    r = db.delete(group_id, ddb_id)
    print(r)

    #print(json.dumps(comp_info, cls=new_alchemy_encoder(), check_circular=False))
    #print(json.dumps(comp_info, cls=AlchemyEncoder, check_circular=False))
    # print(to_dict(comp_info))
    exit(0)
    #g = DbHandler()
    #r = g.group_existed('default')
    # print(r)
    g = Dataflow()
    g.start_plus('')

def test_start_plus():
    from api.test import param_start_plus
    from api.test import param_stop_plus
    from component.dataflow import Dataflow
    g = Dataflow()
    group_id = g.start_plus(param_start_plus)
    return group_id

def test_query(param):
    from component.dataflow import Dataflow
    g = Dataflow()
    status = g.query(param)
    return status

def test_stat():
    from component.stat import Stat
    s = Stat()
    s.query_exchange_data_volume_all()
    s.query_exchange_data_top()

def test_parameter():
    from component.dataflow import Dataflow
    from api.test import param_start_plus1

    g = Dataflow()
    g.merge_capture(param_start_plus1)

def test_dataflow():
    from component.dataflow import Dataflow
    g = Dataflow('dataflow_5')
    #g.create_dataflow()
    #r = g.merged_capture()
    #r = g.query_loader_filter()
    print(r)

def test_db():
    from data_model.db import DbHandler
    db_hdl = DbHandler()
    #db_hdl.set_dataflow_info('dataflow_19', {'e_id':'v', 'l_id':'vv'})
    #r = db_hdl.query_group_id_of_dataflow('dataflow_10')
    #r = db_hdl.query_group_datafolw_count('group_25')
    #r = db_hdl.delete_dataflow_info('dataflow_5')
    #r = db_hdl.delete_dataflow_config('dataflow_5')
    #db_hdl.remove_loader_table(2, [('KYLIND', 'KYLIN', 'TEST', None)])
    #db_hdl.remove_loader_table(2, [('KYLIN', 'KYLIN', 'TEST', None)])
    #r = db_hdl.get_group_loader_list('group_1')
    #r = db_hdl.query_dataflow_scn('dataflow_1')
    r = db_hdl.query_group_loader_list('group_1')
    print(r)

if __name__ == '__main__':
    #test()
    #group_id = test_start_plus()
    #print(group_id)
    # group_id = 'group_4'
    # status = test_query({'group_id': group_id})
    # print(status)
    # test_helper()
    #test_stat()

    #group_id = 'group_4'
    #status = test_query({'group_id': group_id})
    #print(status)
    # test_helper()

    # test_parameter()
    #test_dataflow()
    test_db()
