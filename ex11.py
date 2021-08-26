from random import randint
p = 0
n = int(input('Digite um número:')),int(input('Digite outro número:')),int(input('Digite mais um numero:')), int(input('Digite o último número:'))
print(n)
print(f'O valor 9 apareceu {n.count(9)} vezes ')
print(f'O valor 3 está na {n.index(3)+1}° posição')
for c in n:
    if c % 2 == 0:
        p += 1
print(f'os valores pares foram {p}')
        