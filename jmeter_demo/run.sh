CURDIR=`pwd`
OLD_IFS="$IFS"
#设置分隔符
IFS="," 
#如下会自动分隔
arr=($thread)
#恢复原来的分隔符
IFS="$OLD_IFS"
rm -rf *_out.txt

jmeter_dir="/disk1/guocr/perf_test/apache-jmeter-4.0/extras"
interface_jmx="speech_eval_perf.jmx"
interface_jtl="speech_eval_perf.jtl"

host=`echo $ahost| awk -F':' {'print $1'}`
port=`echo $ahost| awk -F':' {'print $2'}`
echo $host
echo $port

cd $jmeter_dir
for j in `ls $interface_jmx` ; do  sed  -i  "s/HTTPSampler.domain\">[a-z0-9]*/HTTPSampler.domain\">$host/g" $j; done
for j in `ls $interface_jmx` ; do  sed  -i  "s/HTTPSampler.port\">[0-9]*/HTTPSampler.port\">$port/g" $j; done
cd -

for s in ${arr[@]}
do
    echo "parall"$s
    export athread=$s

    export JAVA_HOME=/global/share/java/jdk1.8.0_66;export PATH=$JAVA_HOME/bin:$PATH
    cd $jmeter_dir
    rm -rf  $interface_jtl $CURDIR/html/
    sed -i  "s/num_threads\">[0-9]*/num_threads\">$athread/g" $jmeter_dir/$interface_jmx
    ../bin/jmeter -n -t $interface_jmx -l  $interface_jtl -e -o $CURDIR/html/
    cd -
    python getdata.py

done
