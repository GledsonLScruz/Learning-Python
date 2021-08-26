from PySimpleGUI import PySimpleGUI as sg

#layout-1
sg.theme('Reddit')
layout = [
    [sg.Text('Bem vindo ao sistema de notas!')],
    [sg.Text('insira o nome do aluno:'), sg.Input(key = 'nome', size=(20, 1))],
    [sg.Text('insira a matéria:'), sg.Input(key='materia', size=(20, 1))],
    [sg.Button('Continuar')]
        ]

#Layout-2
sg.theme('Reddit')
layout2 = [
    [sg.Text('Insira as notas referentes ao 1°Trimestre')],
    [sg.Text('Simulado:'),sg.Input(key= 'simulado',size=(20,1))],
    [sg.Text('Parcial:'),sg.Input(key= 'parcial',size=(20,1))],
    [sg.Text('Conclusiva:'),sg.Input(key= 'conclusiva',size=(20,1))],
    [sg.Text('Qualitativa:'),sg.Input(key= 'qualitativa',size=(20,1))],
    [sg.Button('Continuar')]
          ] 
#Janela
janela = sg.Window('Reconhecimento', layout)

#Leitor de Eventos
while True:
    eventos, valores = janela.Read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Continuar':
        if valores ['nome'] == 'gledson' and valores ['materia'] == 'matematica':
            janela = sg.Window('Reconhecimento', layout2)


#sim1tm = float(input("Qual a nota do simulado de {}?".format(nome)))
#simok1tm = sim1tm*0.5
#con1tm = float(input("Qual a nota da conclusiva de {}?".format(nome)))
#conok1tm = con1tm*0.3
#par1tm = float(input("Qual a nota da parcial de {}?".format(nome)))
#parok1tm = par1tm*0.2
#qual1tm = float(input("Qual a qualitativa de {}?".format(nome)))
#qualok1tm = qual1tm* 0.3
#primeiraparte1tm = (simok1tm+conok1tm+parok1tm)*0.7
#nota1tm= primeiraparte1tm+qualok1tm
#print("="*50)
#print("A nota de {} no 1°Trimestre é: {:.3f}!".format(nome, nota1tm))