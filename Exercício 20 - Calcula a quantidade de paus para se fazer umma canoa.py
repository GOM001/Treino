print ('Com quantos paus se faz uma canoa')
qt=int(input('Quantos triputantes a canoa deve abrigar? ')) # quantidade de tripulantes
qe=float(input ('qual o coeficiente de estrutura (de acordo com o nível de navegação) ')) #coeficiente estrutural
q=(qt*qe)/0.4 #quantdade de madeira
print ('você vai precisar de %d metros^2 de táuba 10cm x 100cm'%q)
