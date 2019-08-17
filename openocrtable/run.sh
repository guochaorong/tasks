


OLD_IFS="$IFS"
#设置分隔符
IFS="," 
#如下会自动分隔
arr=($thread)
#恢复原来的分隔符
IFS="$OLD_IFS"

rm -rf *_out.txt

for s in ${arr[@]}
do
    echo "parall"$s
    export athread=$s
    sh parall.sh  $s
    sleep 15m; ps aux| grep single | awk {'print $2'}| xargs kill -9
    python getdata.py        #get data from grafana
    #python getdata_bylog.py  #get data from service log

done



