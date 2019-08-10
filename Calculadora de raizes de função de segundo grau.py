#Clacular função de segundo grau
print('Calculadora de raizes de funçao de segundo grau')
x=0
while x<1:
    a=int(input('Digite o valor de "a":  '))
    b=int(input('Digite o valor de "b":  '))
    c=int(input('Digite o valor de "c":  '))
    delta=((b**2)-(4*(a*c)))
    if delta<0:
           print("sua equação não tem um valor real pois o delta é menor que zero (delta = %f)"%delta)
    else:
        rdelta=delta**0.5
        x1=(-(b)+(rdelta))/(2*a)
        x2=(-(b)-(rdelta))/(2*a)
        print(x1, x2) 
