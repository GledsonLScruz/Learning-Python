from random import randint as random
from time import sleep 

cpc = random(0,2)
print('''\nSUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA\n''')
cuser = int(input('QUAL SUA JOGADA?'))
print('\033[35mJO\033[m')
sleep(1)
print('\033[35mKEN\033[m')
sleep(1)
print('\033[35mPO\033[m')
sleep(0.5)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = lista[cpc]
user = lista[cuser]
print('-='*20)
print(' Computador escolheu {} \n Usuário escolheu {} '.format(pc,user))
print('-='*20)
if pc == user:
    print('\033[36m EMPATE\033[m')
elif pc == 'PEDRA' and user == 'PAPEL':
    print('\033[32mVocê Ganhou!!\033[m')
elif pc == 'PEDRA' and user == 'TESOURA':
    print('\033[31mVocê Perdeu!\033[m')
elif pc == 'PAPEL' and user == 'PEDRA':
    print('\033[31mVocê Perdeu!\033[m')
elif pc == 'PAPEL' and user == 'TESOURA':
    print('\033[32mVocê Ganhou!!\033[m')
elif pc == 'TESOURA' and user == 'PEDRA':
    print('\033[32mVocê Ganhou!!\033[m') 
elif pc == 'TESOURA' and user == 'PAPEL':
    print('\033[31mVocê Perdeu!\033[m')

    
