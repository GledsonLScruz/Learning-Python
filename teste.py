while True:
    num = int(input('Digite um numero inteiro qualquer:'))
    conversor = str(input("""   Qual o método de conversão?
                                - [1] Binário
                                - [2] Octal
                                - [3] Hexadecimal
                                - [X] Sair               """)).strip()
    if conversor == '1' :
        print(bin(num)[2:])
    elif conversor == '2':
        print(oct(num)[2:])
    elif conversor == '3':
        print(hex(num)[2:])
    elif conversor == 'x' or conversor == 'X':
        break
    else:
        print('Opção invalida'),
        break
        









                       