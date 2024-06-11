import PySimpleGUI as sg

sg.theme('DarkGrey8')
sg.set_options(font = 'Franklin 18')
menu_input = [
    'menu', ['DarkAmber, DarkGrey8', 'Python', 'GrayGrayGray']
]

col_1 = [
    [sg.Text('My Contact boob', font = 'Franklin 12')],
    [sg.Text('Welcome Neeraj The great')],
    [sg.Table(values = '', headings = ['Index', 'Phone', 'Contacts'], auto_size_columns= False, col_widths= [5, 20 ,30], justification= 'left' ,key = '-TABLE-')]
]

col_2 = [
    [sg.Text('Enter the name:  '), sg.VPush(), sg.Input(key = '-NAME-', size = (20, 1))],
    [sg.Text('Enter the phone: '), sg.VPush(), sg.Input(key = '-PHONE-', size = (20, 1))],
    [sg.Button('Save', key = '-SAVE-'), sg.Button('Delete', key = '-DEL-')]

]
contacts = []
counter = 1


layout = [
    [sg.Text('Add contact here')],
    [sg.Col(col_2), sg.VerticalSeparator(),sg.Col(col_1)]
]
window = sg.Window('Contact Book', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-SAVE-':
        print(event)
        names = values['-NAME-']
        phones = values['-PHONE-']
        contact = [
            [counter, phones, names]
        ]
        contacts += contact
        window['-TABLE-'].update(contacts)
        window['-NAME-'].update('')
        window['-PHONE-'].update('')
        counter += 1

    if event == '-DEL-':
        index = values['-TABLES-'][0]
        del contacts[index]
        window['-TABLE-'].update(contacts)


window.close()