import os
import sys
import ctypes

# -*- coding: utf-8 -*- https://wiki.python.org.br/CoresNoTerminal
"""
0 = Black          1 = Blue            2 = Green
3 = Aqua           4 = Red             5 = Purple
6 = Yellow         7 = White           8 = Gray
9 = Light Blue     10 = Light Green    11 = Light Aqua
12 = Light Red     13 = Light Purple   14 = Light Yellow

Este código é baseado no software Python Wikipedia Bot, distribuído pela MIT license.

"""

def printColorizedInWindows(text, color):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    for i in range(0, len(color)):
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
        sys.stdout.write(text)
    # cor padrão é 7, white
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle)
    
if __name__ == "__main__":
    text = ("Imprimindo texto colorido no MS-DOS")
    color = [4] # número da cor do texto
    printColorizedInWindows(text, color)

for letra in ["0","1","2","3","4","5","6","7"]:
    for bold in ['',';1']:
        for fundo in ["0","1","2","3","4","5","6","7"]:
            seq="4" + fundo + ";3" + letra
            saida = "\033["+ seq + bold + "m" + (seq+bold).center(8) + "\033[m"
            print ("%s" % saida)
        