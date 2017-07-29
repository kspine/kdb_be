#! /bin/bash

if [ ${DIP_HOME-""} = "" ]; then
    read -p "set DIP_HOME: [/dip]" DIP_HOME
    DIP_HOME=${DIP_HOME:="/dip"}
fi

if [ ${DIP_SERVICE_HOME-""} = "" ]; then
    echo "DIP_SERVICE_HOME not set... "
    DIP_SERVICE_HOME=$(cd `dirname $0`; pwd)
    echo "auto set DIP_SERVICE_HOME=${DIP_SERVICE_HOME}"
    read -p "[Ctrl-c] to EXIT, any key to CONTINUE"
fi

echo "decompress "
cd $DIP_SERVICE_HOME/dep
if [ -f oracle.tgz ]; then
    TGZ=`ls *.tgz`
else
    TGZ="oracle.tgz python36.tgz unixODBC.tgz"
fi
for f in $TGZ; do
    echo "decompress $f ..."
    if [ -d ${f%%.*} ]; then
        continue
    fi
    tar zxf $f
done

cd -

echo "setup env..."
# mysql port
MYSQL_PORT=`sed -n "s/^port *= *\([0-9]\+\)/\1/p" $DIP_HOME/mysql/my.cnf`
sed -i "s/\(^port *= *\).*/\1$MYSQL_PORT/" $DIP_SERVICE_HOME/src/config.cfg

# server port
echo -n "Please input DIP-SERVICE web server port: [8888] "
read web_svr_port
web_svr_port=${web_svr_port:="8888"}

sed -i "s/\(^dip_svc_port *= *\).*/\1$web_svr_port/" $DIP_SERVICE_HOME/src/config.cfg

# unixODBC
sed -i "s#\(^Driver=\).*#\1$DIP_SERVICE_HOME/dep/oracle/odbc/libsqora.so.12.1#" $DIP_SERVICE_HOME/dep/unixODBC/etc/odbcinst.ini

# env
sed -i "s#\(^DIP_SERVICE_HOME=\).*#\1$DIP_SERVICE_HOME#" $DIP_SERVICE_HOME/env
sed -i "s#\(^DIP_HOME=\).*#\1$DIP_HOME#" $DIP_SERVICE_HOME/env

# dip env
sed -i "1iunset LD_LIBRARY_PATH" $DIP_HOME/env

# source $DIP_SERVICE_HOME/env

echo "all done"
