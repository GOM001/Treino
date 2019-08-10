a=1
resultado=int(input('digite o número para saber se é triangular  '))
n=0
while  n < resultado:
    a=a+1
    n=(a*(a+1)*(a+2))
if n==resultado:
    print(' triangular a= %d, b=%d e c=%d' %(a, a+1, a+2))
else:
    print('Não triangular')

    
    
