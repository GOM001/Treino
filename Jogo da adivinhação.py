print("----------------------------------------------------------------")
print("Vou pensar em um número entre  0 e 5. tente adivinhar qual é!")
print("----------------------------------------------------------------")

#Variaveis Declaradas
c=""

#Corpo de Programa
while c != "N":
    a=int(input("Digite o número(0 à 5) que você pensou: "))
    import random
    b=random.randint(0,5)
    if b==a:
        print("Parabéns Você acertou!!! :) também pensei no ", b)
    else:
        print("Você Errou :( Eu pensei no número ",b)
    c=str(input("Deseja continuar? [S/N] ")).upper()
print("Fim do Programa")
