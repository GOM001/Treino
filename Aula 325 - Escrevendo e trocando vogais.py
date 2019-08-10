arquivo=open("cripto.txt","w")
palavra=input("digite uma palavra: ")
arquivo.write("a palavra digitada é: %s"%palavra)
x=0
texto=""
while x<len(palavra):
    if palavra[x] in "aeiou":
        texto=texto+"@"
    else:
        texto=texto+palavra[x]
    x=x+1
arquivo.write("\na palavra reformulada é %s"%texto)
arquivo.close()
with open("cripto.txt") as f:
    for linha in f.readlines():
        print(linha)
