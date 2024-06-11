import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='bold')

    layout = [
        [sg.Text('Right click here', enable_events=True, justification='right', expand_x=True, font='Franklin 30', pad = (10, 20), right_click_menu= theme_menu, key = '-OUTPUT-')],
        [sg.Button('Clear', size=(6, 3), expand_x=True), sg.Button('Enter', size=(6, 3), expand_x=True)],
        [sg.Button(7, size=(6, 3)), sg.Button(8, size=(6, 3)), sg.Button(9, size=(6, 3)), sg.Button('*', size=(6, 3))],
        [sg.Button(4, size=(6, 3)), sg.Button(5, size=(6, 3)), sg.Button(6, size=(6, 3)), sg.Button('/', size=(6, 3))],
        [sg.Button(1, size=(6, 3)), sg.Button(2, size=(6, 3)), sg.Button(3, size=(6, 3)), sg.Button('-', size=(6, 3))],
        [sg.Button(0, size=(6, 3), expand_x=True), sg.Button('.', size=(6, 3)), sg.Button('+', size=(6, 3))]

    ]
    return sg.Window('Calculator', layout)

num = list()
operator = list()

theme_menu = ['menu',['Material1', 'PythonPlus', 'TanBlue', 'random', 'GrayGrayGray', 'Reset']]
window = create_window('DarkGrey8')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event in theme_menu[1]:
        window.close()
        window = create_window(event)
        if event in theme_menu[1][-1]:
            window.close()
            window = create_window('DarkGrey8')
        else:
            pass

    elif event in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        num.append(event)
        all_num = ''.join(num)
        window['-OUTPUT-'].update(all_num)

    elif event in ['+', '-', '*', '/']:
        operator.append(all_num)
        num =[]
        operator.append(event)
        window['-OUTPUT-'].update(event)

    elif event == 'Clear':
        num = []
        operator = []
        window['-OUTPUT-'].update('')

    elif event == 'Enter':
        operator.append(''.join(num))
        result = eval(''.join(operator))
        window['-OUTPUT-'].update(result)
        operator = []


window.close()
