print('Sequência de Fibonacci')
print('~'*20)
n = int(input('Quantos termos você quer mostrar?'))
c = 1
v1 = 1
v2 = 1
print(v1,end = '')
while c <= n:
    v3 = v1 + v2
    v1 = v2
    v2 = v3
    print('', v3 ,end = '')
    c += 1