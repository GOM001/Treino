vetorvog=[]
vetorcon=[]
vetor=[]
contcon=0
contvog=0
repeticao=1
while repeticao<=10:
    letra=input('digite a letra (em minúsculo) ')
    vetor.append(letra)
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        vetorvog.append(letra)
        contcon=contcon+1
    else:
        vetorcon.append(letra)
        contvog=contvog+1
    repeticao=repeticao+1
print('os letras digitadas foram ',vetor)
print('as consoantes são', vetorcon)
print('as Vogais são', vetorvog)
print(' a quantidade de vogais é %d e a de consoantes é %d'%(contcon, contvog))
    
