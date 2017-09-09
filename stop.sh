ps ax | grep kdb.py | grep -v grep | awk '{print $1}' | xargs -i kill -9 {}
