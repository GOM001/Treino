vl=int(input('Velocidade do veículo: '))
if vl<=110:
       print('Você é um Motorista exemplar, Continue dessa forma!')
if vl>110:
    Multa=(vl-110)*5
    print ('você excedeu a velocidade da pista e será multado em R$ %d . sendo o valor da multa de R$ 5,00 para cada quilometro a mais na velocidade e perda de 3 pontos na carteira' %Multa)
       
