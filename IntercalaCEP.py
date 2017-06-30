# -*- coding: utf-8 -*-
'''
Created on 4 de mai de 2017

@author: Flávio
'''

import struct
import os
import math
import time

print time.strftime('%X')

def main():
    
    n = 4000000#numero de registros
    m = 1000000#numero de registros por bloco
    k = math.ceil(n*1.0/m)
    print k
    while k > 1:
        i = 0
        l = 0
        while i < k:
            nomei = "sortGrande/bloco%d.txt" %i
            nomel = "sortGrande/bloco%d.txt" %l
            j = i+1
            if j < k:
                nomej = "sortGrande/bloco%d.txt" %j
                merge(nomei, nomej, "sortGrande/temp.txt")
                os.remove(nomei)
                os.remove(nomej)
                os.rename("sortGrande/temp.txt", nomel)
                
            else:
                os.rename(nomei, nomel)
            l += 1
            i += 2
        k = l
    print time.strftime('%X')
    
def merge(bloco1, bloco2, temp):
    
    registroCEP = struct.Struct("5s5s30s5s5s5s5s14s40s32s10s10s")
    tamanhoRegistro = registroCEP.size
    saida = open(temp, 'w')
    entrada1 = open(bloco1, 'r')
    entrada2 = open(bloco2,'r')
    
    arquivo1 = registroCEP.unpack(entrada1.read(tamanhoRegistro)) 
    arquivo2 = registroCEP.unpack(entrada2.read(tamanhoRegistro))
    intercalando = True
    fimLeitura1 = False
    fimLeitura2 = False  
    
    while (intercalando):
        
        if  arquivo1[7] > arquivo2[7]:
            saida.write(''.join(arquivo2))
            leituraTeste = entrada2.read(tamanhoRegistro)
            if (leituraTeste != ""):
                arquivo2 = registroCEP.unpack(leituraTeste)
                UltimaLeitura2 = leituraTeste
            else:
                fimLeitura2 = True
                
        else:
            saida.write(''.join(arquivo1))
            leituraTeste = entrada1.read(tamanhoRegistro)
            if (leituraTeste != ""):
                arquivo1 = registroCEP.unpack(leituraTeste)
                UltimaLeitura1 = leituraTeste
            else:
                fimLeitura1 = True
        
        if fimLeitura1 == True:
            while (UltimaLeitura2 != ""):
                arquivo2 = registroCEP.unpack(UltimaLeitura2)
                saida.write(''.join(arquivo2))
                UltimaLeitura2 = entrada2.read(tamanhoRegistro)   
                
            intercalando = False
            
        if fimLeitura2 == True:
            while (UltimaLeitura1 != ""):   
                arquivo1 = registroCEP.unpack(UltimaLeitura1)
                saida.write(''.join(arquivo1))
                UltimaLeitura1 = entrada1.read(tamanhoRegistro)
                
            intercalando = False
                     
    entrada1.close()
    entrada2.close()
    saida.close()
    
main()
