ps ax | grep server.py | grep -v grep | awk '{print $1}' | xargs -i kill -9 {}
