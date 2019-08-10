lista=[]
for f in range(1067, 3628):
    if f%2==0 and f%7==0:
        lista.append(f)
print('%d números pares divisiveis por 7' %len(lista))
print(lista)
