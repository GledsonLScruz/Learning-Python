from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário:'), sg.Input(key='usuario',size=(20, 1))],
    [sg.Text('Senha:'), sg.Input(key='senha', password_char = '*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar',size=(20, 1))]
]

#Janela
janela = sg.Window('Tela de Login', layout)

#Leitor de Eventos
while True:
    eventos, valores = janela.Read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuario'] == 'gledson' and valores ['senha'] == '123456':
            print('Bem-Vindo ao Sistema de notas!')