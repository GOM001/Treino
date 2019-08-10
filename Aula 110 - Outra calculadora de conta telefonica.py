print('Calculadora de conta de Telefone Tchau Company')
t=float(input('digite a quantidade de minutos ultilizados '))
if t<=200:
        v=t*0.2
        print('(Tipo 1)sua conta terá o valor de R$ %.2f'%v)
if t<=400 and t>200:
    v=t*0.18
    print('(Tipo 2)sua conta terá o valor de R$ %.2f'%v)
if t>400 :
    v=t*0.15
    print('(Tipo 3)sua conta terá o valor de R$ %.2f'%v)
if t>44640 :
    v=t*0.15
    print('(Tipo 0)Contate nosso serviço de atendimento ao cliente. Sua conta ultrapasssou o limite de minutos o valor de R$ %.2f será cobrado em fatura caso não haja contato'%v)
