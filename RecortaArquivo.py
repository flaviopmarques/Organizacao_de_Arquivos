# -*- coding: utf-8 -*-
'''
Created on 22 de jun de 2017

@author: Fl�vio
'''

fileName = "201704_BolsaFamiliaFolhaPagamento.csv"


lineCount = 0
qtdLinhas = 10000000

f = open(fileName,"r")
fout = open("recorteBolsa201704_10000000.txt", "w")
line = f.readline()
while lineCount < qtdLinhas:
    line = f.readline()
    fout.write(line)
    lineCount += 1
f.close()

print lineCount