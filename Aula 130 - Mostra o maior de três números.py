'''
    comentário de várias linhas
    Faça um programa que leia três números e mostre o maior deles.
'''

A=int(input('Coloque o valor de A '))
B=int(input('Coloque o valor de B '))
C=int(input('Coloque o valor de C '))
if A>=B and A>=C:
    Maior=A
elif B>=A and B>=C:
    Maior=B
else:
    Maior=C
print('O número %.2f é o maior!'%Maior)
            
