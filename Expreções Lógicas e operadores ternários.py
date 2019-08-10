'''
tterca = False
tquinta = False

tv50 = tterca and tquinta
sorvete = tterca or tquinta
tv32 = tterca != tquinta
saudavel = not sorvete

print("Tv50 = {} \nTv32 = {} \nSorvete = {} \nSaudável = {}" .format(tv50,tv32,sorvete,saudavel))


esta_chovendo = True

print('Hoje estou com as roupas ' +('secas','molhadas')[esta_chovendo])#Operador Ternário


print('Hoje estou com as roupas ' +('molhadas' if esta_chovendo else 'secas'))#Operador Ternário

lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)
print('Ana' not in lista)

'''
x = 3
y = x
z = 3
print(x is y)
print(y is not z)
