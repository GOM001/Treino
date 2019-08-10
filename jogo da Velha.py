#Jogo da Velha

#Variaveis
a=''
velha=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Funções Definidas
def reset():
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{velha[l][c]}]', end='')
        print('')

def encontrex(n):
    for l in range(0, 3):
        for c in range(0, 3):
            if velha[l][c] == n:
                velha[l][c] = 'X'
def encontreo(n):
    for l in range(0, 3):
        for c in range(0, 3):
            if velha[l][c] == n:
                velha[l][c] = 'O'
def vitoriax(p):
    if velha[0][0]==velha[0][1]==velha[0][2]:
        print('Parbéns "X" você ganhou')
        p='vitoria'
            
#inicio
input('Vamos Brincar de Jogo da Velha? (enter Para Continuar) ')
reset()
input('Ao iniciar o jogo digite o número que corresponde a Posição em que você quer jogar: (Enter para Continuar)')
input('Vamos Começar?" (Enter Para continuar)')

#Corpo do Programa
while a != 'vitoria':
    b=int(input('Vez do X: '))
    if b>=1 and b<=9:       
        encontrex(b)
        reset()
        vitoriax(a)
    if a!="vitoria":
        b=int(input('Vez do O: '))
        encontreo(b)
        reset()
    else:
        print('DHUUUUUUU')
         
