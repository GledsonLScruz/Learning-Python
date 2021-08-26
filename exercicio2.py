reta1 = float(input('Digite um valor: '))
reta2 = float(input('Digite outro valor: '))
reta3 = float(input('Digite outro valor: '))
if reta1 >  abs(reta2 - reta3) and reta1 < reta2 + reta3:
    print('Pode formar um tringulo')
else:
    print('Não pode formar um triangulo')
        