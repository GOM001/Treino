escreva=input("escreva a palavra:   ")
texto = open("mensagem.txt", "w")
texto.write(escreva)
texto.close()
texto = open("mensagem.txt")
saida = open("cripto.txt", "w")
for linha in texto.readlines():
    for letra in linha:
        if letra in"aeiou":
            saida.write("#")
        else:
            saida.write(letra)
texto.close()
saida.close()
s=open("cripto.txt", "r")
for linha in s.readlines():
    print(linha)
s.close()
