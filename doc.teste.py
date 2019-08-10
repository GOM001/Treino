def dormir(dia_semana, feriado):
    if feriado:
        return True
    elif dia_semana:
        return False
    return True


def alunos_problema(a_sorri, b_sorri):
    if a_sorri and b_sorri:
        return True
    elif a_sorri or b_sorri:
        return False
    return True 

def soma_dobro(a, b):
    if a==b:
        return 2*(a+b)
    return a+b

def diff21(n):
    if abs(n)<=21:
        return 21-abs(n)
    return (abs(21-n))*2

def apaga(s, n):
    b=''
    for a in range(len(s)):
        if s[a]!=s[n]:
            b=b+s[a]
        else:
            b=b+""
    return b 

def troca(s):
    if len(s)<=1:
        return s
    else:
       b=s[len(s)-1]+s[1:(len(s)-1)]+s[0]
    return b
