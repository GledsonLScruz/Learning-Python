nomehomem = 'string'
media = 0
hmv = 0
idh = 0
contador = 0
for i in range(1,5):
    print('-------{}ª pessoa-------'.format(i))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [H/M]')).upper()
    media += idade
    if sexo == 'H':
        if idade > hmv:
            hmv = idade
            nomehomem = nome
            idh = idade
    if sexo == 'M':
        if idade < 20:
            contador += 1
print('A média de idade do grupo é: {}'.format(media/i))
print('O Homem mais velho tem {} anos e é {}'.format(idh,nomehomem))
print('Ao todos são {} mulheres com menos de 20 anos'.format(contador))


