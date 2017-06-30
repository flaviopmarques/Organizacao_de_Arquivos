# -*- coding: utf-8 -*-
'''
Created on 22 de jun de 2017

@author: Fl�vio
'''
import struct
import codecs
import time

print time.strftime('%X')


def PesquisaBinaria(arquivo, chave, tamanhoRegistro, tamanhoArquivo, formato):

    registros = tamanhoArquivo//tamanhoRegistro
    inf = 0             
    sup = registros - 1  
    meio = 0
    flag = False
    while (inf <= sup):
        meio = (inf + sup) // 2
        #print meio
        arquivo.seek(meio*tamanhoRegistro)
        leitura = formato.unpack(arquivo.read(tamanhoRegistro))
        #print leitura[7]
        #print chave
        if (chave == leitura[7]):
            flag = True
        if (chave < leitura[7]):
            sup = meio - 1
        else:
            inf = meio + 1
            
    return flag  



fileName = "recorteBolsa201703_6000000.txt"
binaryName = "Sort/recorteBolsaSort201704_10000000.txt"
dataFormat = "5s5s30s5s5s5s5s14s40s32s10s8s2s"
encoding = "latin1"
keyColumnIndex = 7

dataStruct = struct.Struct(dataFormat)

f = open(fileName,"rb")
num_out = 0

fi = open(binaryName,"rb")
tamanhoRegistro = dataStruct.size
fi.seek(0,2)
tamanhoArquivo = fi.tell()
fi.seek(0)

while True:

    line = f.readline()
    #print line
    if line == "": # EOF
        break
    
    record = line.split("\t")
    nis = codecs.decode(record[keyColumnIndex],encoding)
    
    existe = PesquisaBinaria(fi, nis, tamanhoRegistro, tamanhoArquivo, dataStruct)
    
    if existe == False:
        #print codecs.decode(recordData[7],encoding)
        num_out += 1

fi.close()
print num_out   
f.close()
print time.strftime('%X')






