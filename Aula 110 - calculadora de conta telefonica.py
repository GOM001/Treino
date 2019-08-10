print('Calculadora de conta de Telefone Tchau Company')
t=float(input('digite a quantidade de minutos ultilizados '))
if t<200:
        v=t*0.2
        print('(T1)sua conta terá o valor de R$ %.2f'%v)
else:
        if t<=400:
                v=t*0.18
                print('T2)sua conta terá o valor de R$ %.2f'%v)
        else:
                if t<=800:
                        v=t*0.15
                        print('(T3)sua conta terá o valor de R$ %.2f'%v)
                else:
                        if t>=800:
                                v=t*0.08
                                print('(T0)sua conta terá o valor de R$ %.2f'%v) 
