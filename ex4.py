from time import sleep

print('-='*20)
print('BEM VINDO AO SISTEMA DE NOTAS!')
print('-='*20)

sleep(0.5)

bcdd = ['admin']
acesso, cadastrado = False , False

choice = str(input(' [1] LOGIN \n [2] CADASTRAR-SE'))
while choice not in '12':
        print('Opção Inválida!\n Digite Novamente!')
        choice = str(input(' [1] LOGIN \n [2] CADASTRAR-SE'))

while not acesso:
        if choice == '1':
            user = str(input('Usuário:'))
            senha = str(input('Senha:'))
            while user not in bcdd and senha not in bcdd:
                print('Usuário não cadastrado!')
                sleep(0.5)
                user = str(input('Usuário:'))
                senha = str(input('Senha:'))
            acesso = True

        if choice == '2':
            if not cadastrado:
                nuser = str(input('Digite seu novo usuário:'))
                nsenha = str(input('Digite sua nova senha:'))
                bcdd.append(nuser)
                bcdd.append(nsenha)
                cadastrado = True
                print('Usuário Cadastrado!')
                sleep(0.5)
            else:
                user = str(input('Usuário:'))
                senha = str(input('Senha:'))
                if user in bcdd and senha in bcdd:
                    acesso = True
                else:
                    print('Usuário e senha n coincidem, tente novamente!')
            
print('Bem vindo!')