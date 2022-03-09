import PySimpleGUI as sg

sg.theme('DarkAmber')   # Adicione um toque de cor
# Todas as coisas dentro da sua janela.
layout1 = [  [sg.Text('Entre com seu nome')],
            [sg.Text('NOME: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

layout2 = [  [sg.Text('Idade: '), sg.InputText()],
             [sg.Text('Sexo: '), sg.InputText()],
             [sg.Button('Continuar'), sg.Button('Cancel')]]
# Crie a janela
window = sg.Window('Tela de teste', layout1, size=(500, 300))
window2 = sg.Window('Dados', layout2, size=(300, 500))
# Loop de eventos para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # se o usuário fechar a janela ou clicar em cancelar
        break
    if event == 'Ok':
        window.close()
        while True:
            event, values = window2.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Continuar':
                break
window2.close()
