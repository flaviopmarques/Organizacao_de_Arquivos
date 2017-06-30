# -*- coding: utf-8 -*-
import struct
from operator import itemgetter
import time

print time.strftime('%X')
'''
Created on 26 de abr de 2017

@author: Flávio
'''

def main():
    entrada = open("Formatado/recorteBolsaFormat201704_4000000.txt", 'r+')
    bolsaFormat = struct.Struct("5s5s30s5s5s5s5s14s40s32s10s10s")
    tamanhoRegistro = bolsaFormat.size
    #print tamanhoRegistro
    entrada.seek(0,2)
    tamanhoArquivo = entrada.tell()
    #print tamanhoArquivo
    entrada.seek(0)
    linhas = tamanhoArquivo//tamanhoRegistro
    leitura = entrada.read(tamanhoRegistro)
    
    saida = open('Sort/recorteBolsaSort201704_4000000.txt', 'w')
    bolsa = []
    bolsasort = []

    for i in range(linhas):
        if leitura == "":
            break
        bolsa.append(bolsaFormat.unpack(leitura))
        leitura = entrada.read(tamanhoRegistro)
    
    bolsasort = sorted(bolsa, key=itemgetter(7))

    for bolsa in bolsasort:
        saida.write(''.join(bolsa))

    
    saida.close()
    entrada.close()
    print time.strftime('%X')
    
main()

