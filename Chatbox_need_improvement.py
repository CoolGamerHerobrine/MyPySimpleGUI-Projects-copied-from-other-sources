import PySimpleGUI as sg

sg.theme('green')

layout = [
    [sg.Text('Your output will go here',font= 'Franklin 12' )],
    [sg.Multiline(size = (110, 20), key= '-OUTPUT-')],
    [sg.Multiline(size = (50, 5), font= 'Franklin 14', key = '-INPUT-'), sg.Button( 'Send', size = (7, 3), font = 'Franklin 14', ), sg.Button('Exit', size = (7, 3), font = 'Franklin 14')]

]
window = sg.Window('Chat Window', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Send':
        history = []
        history.append(values['-INPUT-'])
        for values['-INPUT-'] in history:
            window['-OUTPUT-'].update(values['-INPUT-'])
        window['-INPUT-'].update('')


    if event == 'Exit':
        break

window.close()
