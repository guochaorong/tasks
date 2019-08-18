# 接入python脚本发压的新接口
 拉取代码: git clone https://github.com/guochaorong/tasks.git tasks

 cd tasks

 copy一份模板接口： cp -rf  openocrtable  新口名

 **修改项：**

 1.修改接口请求single.py 文件
 ```shell
ahost = os.environ.get('ahost')#要测试的服务器url和port
adata = os.environ.get('adata')#要跑的测试数据路径
#ahost='nc107:9696'
#adata='imgs_dir'
```
2. 如果使用grafana监控获取数据，修改getdata.py文件
```shell
burl = 'openapi.aimini.online.xxx.ocrQuestionRequestForMini.' #待监测服务grafana数据路径
```
3.如果没有监控，则通过日志获取数据，修改getdata_bylog.py文件中：
```shell
targetDir='/disk1/zhiyuntest/asr/logs' #修改成服务日志路径
flog = "springboot.log.2019-08-*"  #修改成服务对应的日志
```
并执行cp -f getdata_bylog.py getdata.py

# 接入jmeter发压的新接口
如果服务没有生成日志，则需通过jmeter脚本实现。

需要使用的模板是 https://github.com/guochaorong/tasks/tree/master/asreval

copy一份模板接口： cp -rf  asreval  新接口名字

修改https://github.com/guochaorong/tasks/blob/master/asreval/run.sh 中，jmeter发压相关文件：
```shell
jmeter_dir="/disk1/guocr/perf_test/apache-jmeter-4.0/extras"
interface_jmx="speech_eval_perf.jmx"
interface_jtl="speech_eval_perf.jtl"
```
# 性能告警阈值设定
在https://github.com/guochaorong/tasks中 各个接口目录，会在接口第一次运行后，自动生成一个latest_kpis文件，里面是各个指标的数据。

在以后的测试中，会和这个测试做diff，如果比当前值变坏了一定的阈值，则这个指标会出现红色的告警。

其中阈值的设定，在各个接口目录的continuous_evaluation.py 文件中

示例
```python
import os
import sys
sys.path.append(os.environ['ceroot'])
from kpi import CostKpi, DurationKpi, AccKpi
##kpy定义在脚本：https://github.com/guochaorong/performance_test/blob/master/tests/kpi.py

p99_kpi = DurationKpi('99', 0.1, actived=True) #0.1代表10%的误差
avg_kpi = DurationKpi('avg', 0.1, actived=True)
qps_kpi = AccKpi('qps', 0.1, actived=True)
#ok_kpi = AccKpi('ok', 0.05, actived=True)

tracking_kpis = [
    p99_kpi,
    avg_kpi,
    qps_kpi,
]
```
上述阈值均默认设定为10%，如果有需要可以根据实际情况调整




