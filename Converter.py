import PySimpleGUI as sg

layout = [
    [sg.Text('Welcome')],
    [sg.Input(key='-INPUT-'), sg.Spin(['Km/Mtr', 'Ltr/Miltr'], key='-SPIN-')],
    [sg.Button('Convert', key='-CONVERT-'), sg.Text(enable_events=True, key='-OUTPUT-')]
]
output = 0

window = sg.Window('Converter', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = float(values['-INPUT-'])
        if values['-SPIN-'] == 'Km/Mtr':
            output = input_value * 1000
            output_string = f'{input_value} Km is {output} in metres'

        elif values['-SPIN-'] == 'Ltr/Miltr':
            output = input_value * 1000
            output_string = f'{input_value} Litre is {output} in mililitre'

        window['-OUTPUT-'].update(output_string)

window.close()