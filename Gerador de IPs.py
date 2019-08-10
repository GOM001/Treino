arquivo=open("IPs.txt", "w")
import random
ip=""
q=int(input("digite a quantidade de IPs a serem gerados:  "))
for b in range(q):
    for x in range(4):
        ip=ip+(str(random.randint(0,350)))
        if x<3:
            ip=ip+"."
        else:
            ip=ip+"\n"
for linha in ip.split("\n"):
    arquivo.write("%s\n"%linha)
arquivo.close()
