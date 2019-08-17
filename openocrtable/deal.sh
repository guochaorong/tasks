ff=/tmp/target
echo "" >  $ff
#for i in {1..$3}
for i in `seq $3`
do
   echo $i 
    min=`date -d "$i minutes ago" | awk {'print $4'}` 

    tmin=`echo $min | awk -F':' {'print $1":"$2'}`
    
    cat $1 | grep $2 | grep $tmin >> $ff
done


qpsmin=`cat $ff|wc -l`
echo "all req: "$qpsmin
qps=$(printf "%.5f" `echo "scale=5;$qpsmin/60/$3"|bc`)
echo "qps: "$qps


mean=`cat $ff | awk -F'costs' {'print $2'} | awk {'print $1'}    |awk '{sum+=$1}END{print "Average = ", sum/NR}'`
echo "mean: "$mean


all=`cat $ff | awk -F'costs' {'print $2'} | awk {'print $1'}  |sort -n | wc -l`
num=`echo "scale=1;$all*0.99" | bc`
nn=`printf "%1.f\n" $num`
echo $num
echo "99num"
echo $nn

p99=`cat $ff | awk -F'costs' {'print $2'} | awk {'print $1'}  |sort -n | sed -n $nn"p"`
echo "p99: "$p99


error=`cat $ff | grep ERROR| wc -l`

echo $error
