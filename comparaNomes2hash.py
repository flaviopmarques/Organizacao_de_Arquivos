# -*- coding: utf-8 -*-
'''
Created on 22 de jun de 2017

@author: Fl�vio
'''
import hashlib
import struct
import codecs
import os
import time

print time.strftime('%X')

hashSize = 12000000
fileName = "recorteBolsa201703_10000000.txt"
indexName = "recorteBolsa201704-hash_10000000.txt"
#dataFormat = "72s72s72s72s2s8s2s"
indexFormat = "14sLL"
encoding = "latin1"
keyColumnIndex = 7

#dataStruct = struct.Struct(dataFormat)
indexStruct = struct.Struct(indexFormat)

def h(key):
    return int(hashlib.sha1(key).hexdigest(),16)%hashSize


f = open(fileName,"rb")
num_out = 0

while True:
    #line = f.read(dataFormat)
    line = f.readline()
    #print line
    if line == "": # EOF
        break
    #recordData = struct.unpack(dataFormat, line)
    recordData = line.split("\t")
    nis = codecs.decode(recordData[keyColumnIndex],encoding)
    
    p = h(nis)
    offset = p*indexStruct.size
    flagExiste = False
    fi = open(indexName,"rb")
    while True:
        fi.seek(offset,os.SEEK_SET)
        indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
        if indexRecord[0] == nis:
            flagExiste = True
            break
        offset = indexRecord[2]
        if offset == 0:
            break
    fi.close()
    
    if flagExiste == False:
        #print codecs.decode(recordData[7],encoding)
        num_out += 1

print num_out   
f.close()
print time.strftime('%X')






