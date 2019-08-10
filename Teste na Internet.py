# Programa Imprimi Emojis em uma página da Web

import os     #Importa biblioteca os
import emoji   #Importa biblioteca emoji

x=0 # define o contador do while mais abaixo como zero

with open('test.htm','w',encoding='utf-8-sig') as f:
    '''
    ("open (arquivo.html) como f"  faz o programa abrir um aquivo com o nome escolhido e a caracteristica
    (.html .mp3 .pdf) e nomeia o arquivo de f no sistema).

    o resto ainda não entendo muito bem essa parte e nem do with
    '''
    while x<10:   # Enquanto o x for menor que 10 a função vai se repetir
        x=x+1
        f.write("Nada")
            
    f.write('\U0001f44d')
    f.write(emoji.emojize('Python is :thumbs_up:'))
    f.write(emoji.emojize( 'Python é :cookie:' ))
    f.write(emoji.emojize( 'Python é :shit:' ))
os.startfile('test.htm')
