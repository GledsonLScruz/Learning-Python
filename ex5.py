from time import sleep 
print('BEM VINDO!')
sleep(0.5)
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
choose = 0
while choose not in [5]:
    choose = str(input('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGAMA\n      '))
    if choose in '1':
        print('      \033[31mA SOMA É\033[m {}'.format(n1+n2))
    elif choose in '2':
        print('      \033[31mA MULTIPLICAÇÃO É\033[m {}'.format(n1*n2))
    elif choose in '3':
        if n1 > n2:
            print('      \033[31mO MAIOR NUMERO É\033[m {}'.format(n1))
        else:
            print('      \033[31mO MAIOR NUMERO É\033[m {}'.format(n2))
    elif choose in '4':
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
    elif choose in '5':
        choose = 5

print('\nFINALIZANDO...')
sleep (1)
print('Obrigado pro utilizar nosso sistema!')