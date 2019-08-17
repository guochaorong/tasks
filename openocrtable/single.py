# -*- coding: utf-8 -*-
import os
import sys
import uuid
import requests
import base64
import hashlib
import time
import json
reload(sys)
sys.setdefaultencoding('utf-8')

ahost = os.environ.get('ahost')
adata = os.environ.get('adata')

APP_KEY = 'xxx'
APP_SECRET = 'xxx'

def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def connect():
    images = os.listdir(adata)
    for i in range(0,20000000):
        for ff in images:
            f = open(r'%s/%s' % (adata, ff), 'rb')  # 浜岃繘鍒舵柟寮忔墦寮€鍥炬枃浠?
            q = base64.b64encode(f.read())  # 璇诲彇鏂囦欢鍐呭锛岃浆鎹负base64缂栫爜
            f.close()

            data = {}
            data['q'] = q
            data['appKey'] = APP_KEY
            curtime = str(int(time.time()))
            data['curtime'] = curtime
            salt = str(uuid.uuid1())
            signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
            sign = encrypt(signStr)
            data['type'] = '1'
            data['salt'] = salt
            data['sign'] = sign
            data['signType'] = 'v2'
            data['docType'] = 'json'
            data['osType'] = 'api'
            for k, v in data.items():
                if k != 'q':
                    print k, v
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post("http://%s/ocr_table" % ahost, data=data)
            try:
                print json.loads(response.content)['errorCode']
            except Exception as e:
                print e

if __name__ == '__main__':
    connect()


