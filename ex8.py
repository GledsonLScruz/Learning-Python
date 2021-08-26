n = int(input('Digite um numero [999 para parar]:'))
parar = False
c = 1
while not parar:
    n1 = int(input('Digite um numero [999 para parar]:'))
    if n1 == 999:
        parar = True
    else:    
        n += n1
        c += 1
print('VOCÊ DIGITOU {} NUMERO E A SOMA ENTRE ELES FOI {}'.format(c,n))
