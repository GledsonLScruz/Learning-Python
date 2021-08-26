from random import randint
c = 0
while True:
    print('-='*20)
    print('VAMOS JOGAR UM IMPAR OU PAR')
    print('-='*20)
    n = int(input('DIGITE UM VALOR:'))
    if n < 0:
        break
    p = input('PAR OU IMPAR? [P/I]').upper()
    pc = randint(0,10)
    print(f' VOCÊ JOGOU {n} E O PC JOGOU {pc}. TOTAL DE {n+pc} ',end = '')
    if (n+pc) % 2 == 0:
        print('DEU PAR')
        if p == 'P':
            print('você ganhou!')
            c +=1
        else: 
            print('Você perdeu!')
    else:
        print('DEU IMPAR')
        if p =='I':
            print('Você ganhou!')
            c +=1
        else:
            print('Você perdeu!') 
print(f'Você ganhou {c} vezes!')
