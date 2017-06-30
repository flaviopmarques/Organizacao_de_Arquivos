# -*- coding: utf-8 -*-
'''
Created on 22 de jun de 2017

@author: Fl�vio
'''
fileName = "201704_BolsaFamiliaFolhaPagamento.csv"
import time

lineCount = 0
qtdLinhas = 3

f = open(fileName,"r")
while lineCount < qtdLinhas:
    line = f.readline()
    print line
    print line.split("\t")
    lineCount += 1
f.close()

print lineCount
print time.strftime('%X')
