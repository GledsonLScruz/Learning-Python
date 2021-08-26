print('Gerador de PA')
print('-='*10)
a1 = int(input('Primeiro Termo:'))
r = int(input('Qual a razão da PA:'))
c = 1
total = 0
mais = 10
while mais != 0: 
    total += mais 
    while c <= total:
        print(a1 + (c - 1) * r, end = '')
        print(' -> ', end = '')
        c += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('fim')
