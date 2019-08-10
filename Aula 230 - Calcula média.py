n=1
soma=0
x=int(input(' De quantos números vai tirar a média?  '))
while n<=x:
    c=int(input('digite o %d número ' %n))
    soma=soma+c
    n=n+1
media=(soma/x)
print('a média é %.2f' %media)
