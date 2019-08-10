print("transformador de Palavra")
palavra=input("Digite a palavra ou sentença a ser alterada ")
x=0
texto=" "
while x<len(palavra):
    if palavra[x] in 'aeiou':
        texto= texto+"*"
    else:
        texto= texto+palavra[x]
    x=x+1
print('a palavra transformada é', texto)
