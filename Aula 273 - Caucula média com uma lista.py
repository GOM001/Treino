cont=int(input('digite o número de notas a comporem a média '))
x=1
soma=[]
while x<=cont:
    nota=float(input('digite a nota %d ' %x))
    soma.append(nota)
    x=x+1
x=0
y=0
while x<cont:
    y=y+soma[x]
    x=x+1
media=y/cont
print('a notas são ', soma, 'e a média é%5.2f'%media)
