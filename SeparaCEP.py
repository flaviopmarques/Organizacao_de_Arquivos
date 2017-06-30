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
    entrada = open("Formatado/recorteBolsaFormat201704_4000000.txt", 'r')
    registroCEP = struct.Struct("5s5s30s5s5s5s5s14s40s32s10s10s")
    tamanhoRegistro = registroCEP.size
    print tamanhoRegistro
    entrada.seek(0,2)
    tamanhoArquivo = entrada.tell()
    print tamanhoArquivo
    entrada.seek(0)
    leitura = entrada.read(tamanhoRegistro)
    bloco = 0 
    
    while (leitura != ""):
        nome = "bloco%d.txt" %bloco
        saida = open(nome, 'w')
        Cep = []
        cepsort = []
    
        for i in range(1000000):
            if leitura == "":
                break
            Cep.append(registroCEP.unpack(leitura))
            leitura = entrada.read(tamanhoRegistro)
        
        cepsort = sorted(Cep, key=itemgetter(7))
    
        for cep in cepsort:
            saida.write(''.join(cep))
    
        print bloco
        bloco += 1
        
        saida.close()
        
    entrada.close()  
    print time.strftime('%X')
    
main()

