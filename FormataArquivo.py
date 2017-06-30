# -*- coding: utf-8 -*-
'''
Created on 22 de jun de 2017

@author: Fl�vio
'''
import struct
import time

print time.strftime('%X')

fileName = "recorteBolsa201704_4000000.txt"
bolsaFormat = "5s5s30s5s5s5s5s14s40s32s10s10s"
#bolsaFormat = "5s25s30s15s20s20s15s20s50s35s15s20s1s"
record = struct.Struct(bolsaFormat)
lineCount = 0
f = open(fileName,"r")
fout = open("Formatado/recorteBolsaFormat201704_4000000.txt", "w")

while True:    
    line = f.readline().rstrip()
    if line == "":
        break
    x = line.split("\t")
    #print x[0]
    #print line.split("\t")
    emptyIndexRecord = record.pack(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11])
    #emptyIndexRecord = record.pack(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11], '\n')
    fout.write(emptyIndexRecord)
    
f.close()
fout.close()
print time.strftime('%X')