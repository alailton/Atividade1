'''
Created on 9 de mar de 2017 eheuh

@author: Alailton (alailton23@gmail.com)
'''

from math import log 

number = int(input("Tamanho da mensagem :"));

bits = int( log( number, 2) + 1);

print("Qtd de bits = {0}".format(bits));
