import os
os.system('cls') or None
import PySimpleGUI as sg
def tri(r1, r2, r3):
    if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
        print(f'Os seguimentos {r1, r2, r3} formam um triangulo ',end=(""))
        if r1 == r2 == r3:
            print('Equilátero. Todos os lados iguais.')
        elif r1 != r2 != r3 != r1:
            print('Escaleno. Todos os lados são diferentes.')
        else:
            print('Isósceles. Dois lados iguais')
    else:
        print(f'Os seguimentos {r1, r2, r3} não formam um triângulo.')


sg.theme('DarkAmber')   
layout1 = [  [sg.Text('Lados do triangulo')],
            [sg.Text('Lado1: '), sg.InputText()],
            [sg.Text('Lado2: '), sg.InputText()],
            [sg.Text('Lado3'),   sg.InputText()],
            [sg.Button('Testar'), sg.Button('Cancel')] ]

layout2 = [  [sg.Text(f'Os segmentos {"Lado1", "Lado2","Lado3"} formam um Triângulo')],
            [sg.Button('Continuar'), sg.Button('Cancel')]]
# Crie a janela
window = sg.Window('TRIANGULO', layout1,)
window2 = sg.Window('RESULTADO', layout2)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
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

