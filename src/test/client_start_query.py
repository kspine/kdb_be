import json
import urllib.parse
import urllib.request
import sys
# from api.test import param_stop_plus
sys.path.append('.')
from api.test import param_start_plus

port=8889
#port=8888

ip = "172.16.6.36:{}".format(port)
ip = "127.0.0.1:{}".format(port)



#
#url = "http://{}/query_group_status".format(ip)
#

#url = "http://{}/query_exchange_data_top".format(ip)
#url = "http://{}/query_exchange_data_volume_all".format(ip)

def send(url, req_dict):
    req_json = json.dumps(req_dict)
    req_post = req_json.encode('utf-8')
    # print(req_post)
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(url=url, headers=headers, data=req_post)
    res = urllib.request.urlopen(req)
    res = json.loads(res.read().decode('utf-8'))
    return res

def start():
    url = "http://{}/start_plus".format(ip)
    req_dict = param_start_plus
    res = send(url, req_dict)
    print(res)
    return res['group_id']

def stop(df_id):
    url = "http://{}/stop_plus".format(ip)
    req_dict = {'group_id': df_id}
    n = 1
    nn = 1
    res = send(url, req_dict)

def query_step(df_id):
    url = "http://{}/query_start_plus_step".format(ip)
    req_dict = {'group_id': df_id, 'id': 1}

    res = send(url, req_dict)

    res = res['step']
    if isinstance(res, list):
        for i in res:
            print(i)
    else:
        print(res)

def query(df_id):
    url = "http://{}/query_group_status".format(ip)
    req_dict = {'group_id': df_id}

    res = send(url, req_dict)
    print(res)

if __name__ == '__main__':
    #df_id = start()
    df_id = 'dataflow_1'
    query(df_id)
