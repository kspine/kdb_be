import threading
from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ThreadPoolExecutor
# https://docs.python.org/3/library/concurrent.futures.html

g_rlock = threading.RLock()
g_rlock_src_db = threading.RLock()
g_rlock_dst_db = threading.RLock()
g_rlock_data = threading.RLock()
g_rlock_data_merge = threading.RLock()

g_data = {}
# {'comp_id':count}, count equal 1, means not merged
g_data_merge = {}

g_data_comp_stop = {}
g_executor = ThreadPoolExecutor(max_workers=8)
