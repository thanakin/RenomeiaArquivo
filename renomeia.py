import os
import sys

if os.path.isfile('config-local.ini'):
    os.rename('config.ini', 'config-remoto.ini')
    os.rename('config-local.ini', 'config.ini')
    print('Utilizando configuração local')
    sys.exit()
elif os.path.isfile('config-remoto.ini'):
    os.rename('config.ini', 'config-local.ini')
    os.rename('config-remoto.ini', 'config.ini')
    print('Utilizando configuração remota')
    sys.exit()
else:
    print('Arquivo nao localizado')

#Alguns testes previos...
'''
import os.path
os.path.isfile('config.ini')
'''

'''
try:
   with open('config.ini', 'r') as f:
       processar_arquivo(f)
except IOError:
    print ('Arquivo não encontrado!')
'''

'''
import os.path
try:
    os.path.isfile('config.ini')
    print('Arquivo existe')
except:
    print('Arquivo nao existe')
'''