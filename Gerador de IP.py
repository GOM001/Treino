import random
arquivo=open("IPs.txt","w")
ip=""
for g in range(30):
    for x in range(4):
        ip=ip + (str(random.randint(0,350)))
        if x<3:
            ip=ip + (".")
        else:
            ip=ip+("\n")
arquivo.write("%s\n"%ip)
arquivo.close()
