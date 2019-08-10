tabuada=1
while tabuada<=10:
    contador=input('Digite enter para iniciar a tabuada do %d' %tabuada)
    n=1
    print('Tabuada do %d' %tabuada)
    while n<=10:
        print('%d x %d = %2.f' %(tabuada,n,tabuada*n))
        n=n+1
    tabuada=tabuada+1
        
