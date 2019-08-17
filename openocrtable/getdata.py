#!/usr/bin/python
#coding:utf-8
import base64
import os, sys
import json
import time
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib, urllib2

burl = 'openapi.ocr_table.test.xxx.callOcrTableApiForHttp.'
#burl = 'openapi.aimini.online.xxx.ocrQuestion.'
kpis = {'qps': 'm1_rate', '99': 'p99', 'avg': 'mean', 'max': 'max'}


GRAPHITE_ADDR="XXX"


for k, v in kpis.items() :
    query = burl + v
    print query
    start = '-10min'
    
    data={'target': query, 'from': start, 'format': 'json'}
    print data
    result = urllib.urlopen(url=GRAPHITE_ADDR, data=urllib.urlencode(data))
    #fout = "./result/" + str(i + start)
    content = result.read()
    cdict = json.loads(content)
    addlist = []
    for item in cdict[0]['datapoints']:
        print item[0]
        if item[0] != None and float(item[0]) > 0:
            addlist.append(float(item[0]))
    ct = ''
    if addlist == []:
        ct = '0'
    else:
        print addlist[1:-1]
        ss = sum(addlist[1:-1])
        length = len(addlist[1:-1])
        if length != 0:
            ct = str(ss/length)
        print ct
    
    dst = '%s_out.txt' % k
    dd = {}
    if os.path.exists(dst):
        try:
            with open(dst, 'r') as f:
                dd = json.load(f)
        except Exception as e:
            print e
    athread = os.environ.get('athread')
    dd[athread] = ct
    with open(dst, 'w') as f:
        json.dump(dd, f)




