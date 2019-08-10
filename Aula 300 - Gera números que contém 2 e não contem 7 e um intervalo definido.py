lista=[]
n=0
for f in range(18644, 33088): #nomeia f do primeiro ao segundo intervalo
    if "2" in str(f) and "7" not in str(f) :
        lista.append(str(f))
        n=n+1
print('foram encontrados %d números da sorte' %n)
