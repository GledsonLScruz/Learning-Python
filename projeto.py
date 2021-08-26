#Projeto fazer o sistema de notas da escola
#Simulado 50% conclusiva 30% parcial 20%=70%, 30%qualitativa.
from time import sleep

#constantes:

separador = '-=-'*20
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'vermelho' :'\033[31m',
         'roxo' : '\033[35m',
         'amarelo' : '\033[33m'}
sim   = []
con   = []
par   = []
quat  = []
media = []

#login

print('-='*20)
print('BEM VINDO AO SISTEMA DE NOTAS!')
print('-='*20)

sleep(0.5)

bcdd = ['admin']
acesso, cadastrado = False , False

choice = str(input(' [1] LOGIN \n [2] CADASTRAR-SE'))
while choice not in '12':
        print('Opção Inválida!\n Digite Novamente!')
        choice = str(input(' [1] LOGIN \n [2] CADASTRAR-SE'))

while not acesso:
        if choice == '1':
            user = str(input('Usuário:'))
            senha = str(input('Senha:'))
            while user not in bcdd and senha not in bcdd:
                print('Usuário não cadastrado!')
                sleep(0.5)
                user = str(input('Usuário:'))
                senha = str(input('Senha:'))
            acesso = True

        if choice == '2':
            if not cadastrado:
                nuser = str(input('Digite seu novo usuário:'))
                nsenha = str(input('Digite sua nova senha:'))
                bcdd.append(nuser)
                bcdd.append(nsenha)
                cadastrado = True
                print('Usuário Cadastrado!')
                sleep(0.5)
            else:
                user = str(input('Usuário:'))
                senha = str(input('Senha:'))
                if user in bcdd and senha in bcdd:
                    acesso = True
                else:
                    print('Usuário e senha n coincidem, tente novamente!')
            

#Introdução

print(separador)
print("\033[36m Bem vindo ao sistema de notas! \033[m")
print(separador)

nome = str(input("insira o nome do aluno desejado:")).strip().lower().capitalize()
materia = str(input("Insira a materia:")).strip().lower().capitalize()

print(separador)

print('{}CARREGANDO...{}'.format(cores['vermelho'], cores['limpa']))
sleep(1.5)

#Trimestres
for t in range(0,3):
      print("Insira as notas respectivas ao {}°Trimestre de {}{}{}".format(t+1,cores['roxo'],nome,cores['limpa']))
      s = float(input("Qual a nota do simulado de {}{}{}?".format(cores['roxo'],nome,cores['limpa'])))
      sim.append(s)
      c = float(input("Qual a nota da conclusiva de {}{}{}?".format(cores['roxo'],nome,cores['limpa'])))
      con.append(c)
      p = float(input("Qual a nota da parcial de {}{}{}?".format(cores['roxo'],nome,cores['limpa'])))
      par.append(p)
      q = float(input("Qual a qualitativa de {}{}{}?".format(cores['roxo'],nome,cores['limpa'])))
      quat.append(q)
      m = ((sim[t]*0.5)+(con[t]*0.3)+(par[t]*0.2)*0.7)+(quat[t]*0.3)
      media.append(m)
      print(separador)
      print("A nota de {} no {}°Trimestre é: {:.2f}!".format(nome,t+1, m))
      print(separador)

print('{}CARREGANDO...{}'.format(cores['vermelho'], cores['limpa']))
sleep(1.5)

#Boletim
print("{}               1° TRIMESTRE     2° TRIMESTRE     3°TRIMESTRE    \n "
      "CONCLUSIVA:            {}              {}              {}         \n"
      " PARCIAIS:              {}              {}              {}         \n"
      " SIMULADOS:             {}              {}              {}         \n"
      " QUALITATIVAS:          {}              {}              {}         \n"
      " MÉDIA:                {:.1f}             {:.1f}             {:.1f}       {}"
      .format(cores['amarelo'],con[0],con[1],con[2],
              par[0],par[1],par[2],
              sim[0],sim[1],sim[2],
              quat[0],quat[1],quat[2],
              media[0],media[1],media[2],cores['limpa']))
print('')
mediafinal = (media[0]+media[1]+media[2])/3
print('')
print('MÉDIA FINAL: {:.1f} '.format(mediafinal))

if mediafinal >=8:
      print('{} Parabéns {}, você foi um aluno excelente e está aprovado{}!'.format(cores['azul'],nome,cores['limpa']))
else:
      print('{}{} você não foi um bom aluno! acaba de ser reprovado.{}'.format(cores['vermelho'],nome,cores['limpa']))

print('')
print('{}DESLIGANDO...{}'.format(cores['vermelho'], cores['limpa']))
sleep(3)
