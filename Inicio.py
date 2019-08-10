print('Hellow Word')

'''
Elaborar um programa que execute musica apartir de
um endereço na web e que seja necessário login e se
nha para asessalo e que seja possivel casdastras n
ovos usuarios.
'''

user_list=[]
senha_list=[]
x=0
z=0

def user(nome):
        user_list.append(nome)

while x == 0:
    up=str(input('Digite o seu nome de usuário:  '))
    if up not in user_list:
        resposta=str(input('deseja se cadastrar? [S/N]  ')).upper()
        if resposta == 'S':
            while z == 0:
                up=str(input('Digite Seu Nome:  '))
                if up not in user_list:
                    user(up)
                    senha = int(input('Digite sua Senha numéria de 4 digitos:  '))
                    senha_list.append(senha)
                    print('Cadastro realizado oom sucesso! ')
                    input('precione Enter para continuar  ')
                    z += 1
                else:
                    print('nome invalido! :(  Tente novamente  ')
                    input('precione Enter para continuar  ')
        elif resposta == ('N'):
            print('Tente Novamente')
            input('Digite enter para proseguir  ')
    else:
        senha = int(input('Digite sua senha: '))
        if senha in senha_list:
            login=True
            x += 1
        else:
            print('Senha Incorreta  ')
            input('Digite Enter para sai proseguirr ')

if login:
    print('Faz qualquer coisa que se faça logado  ')
print(user_list, senha_list)

