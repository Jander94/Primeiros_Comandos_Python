import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Checkbox

sg.theme('Darkgreen2')

layout1 = [ [sg.Text('Calculadora')],

            [sg.Input()],

            [sg.Input()],
            
            [sg.Button('SOMAR')],
            
            [sg.Button('SUBTRAIR')],

            [sg.Button('Sair')],

            [Checkbox('Gravar dados')]

]
janela1 = sg.Window('Calculadora 2', layout1, size=(500,300))

while True:
    event, values = janela1.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    
janela1.close()