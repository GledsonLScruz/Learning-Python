print('{}{}{}'.format('-='*10,'\n10 TERMOS DE UMA PA\n','-='*10))
pt = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a razão: '))
an = pt+(10-1)*razao
for c in range(pt, an+1, razao):
    print(c,'->', end=' ')
print('ACABOU')