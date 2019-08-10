print("El Vidente")
print("Pergunte algo e receba uma resposta de Sim ou Não")
import random
for n in range(10):
    per=input("Qual a sua pergunta? ")
    x=random.choice(["Sim", "Não"])
    print(" A resposta para ",per," é ",x)
