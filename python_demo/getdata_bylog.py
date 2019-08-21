import json
import os
import subprocess
import time

targetDir='/disk1/zhiyuntest/asr/logs'
flog = "springboot.log.2019-08-16*"

def RunCmd(cmd, shellformat = True):
    p = subprocess.Popen(cmd, shell=shellformat, close_fds=True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout,stderr = p.communicate()
    return (p.returncode, stdout, stderr)

def genjson(key, k, out):
    dst = '%s_%s_out.txt' % (key, k) 
    dd = {}
    if os.path.exists(dst):
        try:
            with open(dst, 'r') as f:
                dd = json.load(f)
        except Exception as e:
            print e
    athread = os.environ.get('athread')
    dd[athread] = out
    with open(dst, 'w') as f:
        json.dump(dd, f)

ttime=int(os.environ.get('atime'))/60
print ttime

mydeal="%s/deal.sh" % (os.path.dirname(os.path.abspath(__file__)))

keys = ["youdaoAsr", "session_time", "afterConnectionEstablished"]
for key in keys:
    cmd='''ssh zj131 "cd %s; sh %s %s  %s %s| grep mean |awk -F'=' {'print \$2'}" '''% (targetDir,mydeal,flog,key, ttime)
    ret,out,err  = RunCmd(cmd) 
    print cmd,ret,out,err
    genjson(key, 'avg', out.strip())
    print "======== ======="
    cmd='''ssh zj131 "cd %s; sh %s %s  %s %s| grep qps |awk -F':' {'print \$2'}" ''' % (targetDir, mydeal,flog,key,ttime)
    ret,out,err = RunCmd(cmd)
    print cmd,ret,out,err
    genjson(key, 'qps', out.strip())
    print "======== ======="

    cmd='''ssh zj131 "cd %s; sh %s %s  %s %s| grep p99 |awk -F':' {'print \$2'}" ''' % (targetDir, mydeal, flog,key,ttime)
    ret,out,err = RunCmd(cmd)
    print cmd,ret,out,err
    genjson(key, '99', out.strip())

