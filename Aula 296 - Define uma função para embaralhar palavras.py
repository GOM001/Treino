p=input("digite a palavra ")
for U in range(20):
    def embaralha(p):
        import random
        lista=list(p)
        random.shuffle(lista)
        return "".join(lista)
    print(embaralha(p))
