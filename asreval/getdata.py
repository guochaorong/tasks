import os
import json

athread = os.environ.get('athread')

kpis = {'Throughput': 'qps',  '99th pct': '99', \
        'Average': 'avg', 'Error %': 'err', \
       }

with open('html/content/js/dashboard.js') as f:
    lines = f.readlines()

dest={}

for line in lines:
    if 'statisticsTable' in line:
        #print line
        td =  ','.join(line.split(',')[1:-2])
        dd = json.loads(td)
        print dd
        for i in range(0, len(dd['titles'])):
           dest[dd['titles'][i]] = dd['items'][0]['data'][i]

print "-----"
print dest

for k, v in kpis.items():
    dst = '%s_out.txt' % v
    dd = {}
    if os.path.exists(dst):
        try:
            with open(dst, 'r') as f:
                dd = json.load(f)
        except Exception as e:
            print e
    dd[athread] = dest[k]
    with open(dst, 'w') as f:
        json.dump(dd, f)

