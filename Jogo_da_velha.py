import random

# Listas de Palavras e Dicas
filmes_marvel = ['Homem Aranha', 'Avengers', 'Homem de Ferro']
frutas = ['Banana', 'Maça', 'Uva']
dicas = [filmes_marvel, frutas]

dica = random.choice(dicas)
palavra = random.choice(dica)
