# coding: utf8

import subprocess
from random import randint
import multiprocessing as mp

PORT = 22

def get_ip():
    return '.'.join([str(randint(0, 255)) for _ in xrange(4)])

def get_range_ip(iterator):
    ip_range = []
    for iter in iterator:
        ip_range.append(get_ip())
    return ip_range

def execute(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    res = p.communicate()[0]
    return res

def worker(ip, port):
    res = execute('nc %s %s -v -w 1 2>&1' % (ip, port))
    if 'succeeded!' in res:
        print(res)
    return

jobs = []
for ip in get_range_ip(xrange(10000)):
    p = mp.Process(target=worker, args=(ip, PORT))
    jobs.append(p)
    p.start()
