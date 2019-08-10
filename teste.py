user_list=[]
senha_list=[]
x=0
z=0

def user(nome):
        user_list.append(nome)

while x == 0:
    up=str(input('Digite o seu nome de usuário:  '))
    if up not in user_list:
        resposta=str(input('deseja se cadastrar? [S/N]  ').upper)
        print(resposta)
