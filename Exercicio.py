import random
import time
num = random.randint(0,6)
print('-=-'*20)
resposta = int(input('A maquina escolheu um numero inteiro de 0 a 5, qual foi ele? '))
print('PROCESSANDO...')
time.sleep(3)
if resposta == num:
    print('Parabéns! você acertou o numero escolhido, ({})'.format(num))
else:
    print('oh não, você errou! o numero certo era ({})'.format(num)) 

