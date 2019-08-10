'''
A idéia nesse programa é que:
    *O usúario escolha entre número da sorte e delimite o intervalo
        desses números
    *Encontre respostas de sim ou não para suas perguntas.
    *Escolha entre quaisquer caracteres para compor uma lista com
    palavras a serem sorteadas.
O usúario poderá escolher qual das modalidades lhe conver e devera sair
dela sem deixar o programa quando for de seu agrado.
'''
import random #importa random
print("Pergunte a sua sorte") #exibe na tela("pergunte a sua sorte")
l=0
lista=[]
while l<=1:
        x=0
        s=input("Digite a letra 'N' para números da sorte, 'SN' para jogo do sim ou não ou 'SE' para sua propria seleção de sorte:  ")#determina a entrada de um valor pelo usúario acompanda do texto entre ('')
        if s.lower()=='n':
                while x<1:
                    c=int(input("quantos números da sorte você deseja sortear?  "))
                    i, ie=input("digite o intervalo de números separado por espaço: exemplo(0 100)  ").split(" ")
                    while x<=c:
                        d=random.randint(int(i), int(ie))
                        if d not in lista:
                                lista.append(d)
                                x=x+1                
                print('os números sorteados foram \n%s' %lista)
        elif s.lower()=='sn':
                while x<1:
                        g=["Sim",  "Não"]
                        c=input("Escreva sua pergunta:  ")
                        d=random.choice(g)
                        print(c, d)
                        u=input("digite enter para fazer outra pergunta ou ' 0 ' (zero) para voltar ao menu inicial   ")
                        if u == "0":
                                break
            
            
