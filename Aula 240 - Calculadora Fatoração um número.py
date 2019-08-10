n=int(input('digite o número a ser fatorado  '))
s=1
x=1
while s<n:
      print('%d*%d'%(x,s+1))
      x=x*(s+1)
      s=s+1
print('o resultado da fatoração é ', x)
