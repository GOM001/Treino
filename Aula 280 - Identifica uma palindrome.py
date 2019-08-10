print('Verificador de Palíndromes')
palavra=input('digite a palavra a ser conferida ')
palindrome=palavra[::-1]
if palavra!=palindrome:
    print('A palavra digitada NÃO é pallindrome','digitada',palavra,'invertida',palindrome)
else:
    print('A palavra digitada é pallindrome','digitada',palavra,'invertida',palindrome)
