v1 = int(input('Digite um valor:'))
d = str(input('Quer Continuar? [S/N]')).upper()
maior = v1
menor = v1
c = 1
m = v1
while d not in 'N':
    v1 = int(input('Digite um valor:'))
    if v1 > maior:
        maior = v1
    elif v1 < menor:
        menor = v1
    c += 1
    m += v1
    d = str(input('Quer Continuar? [S/N]')).upper()
print('Você digitou {} números e a média foi {:.2f}'.format(c, m/c))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior,menor))