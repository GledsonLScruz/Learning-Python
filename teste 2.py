print('{:=^50}'.format('LOJAS GUANABARA'))
valor = float(input('Preço das compras: R$'))
opção = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?'''))
if opção == '1':
     print('{}'.format(valor*0.90))
elif opção == '2':
     print('{}'.format(valor*0.95))
elif opção == '3':
     print('{}'.format(valor))
elif opção == '4':
     print('{}'.format(valor*1.20))


