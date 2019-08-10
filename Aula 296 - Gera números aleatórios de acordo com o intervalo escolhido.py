print("Gerador de números aliatórios")
par=int(input("Números a sortear: "))
x, y=input('digite o intervalo a ser tomado separado por ",": ').split(",")
for N in range(par):
    import random
    print(random.randint(int(x),int(y)))
