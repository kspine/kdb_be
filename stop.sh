ps ax | grep kdb.py | grep -v grep | cut -d " " -f 1 | xargs -i kill -9 {}
