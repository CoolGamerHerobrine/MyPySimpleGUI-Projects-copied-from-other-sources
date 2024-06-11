import PySimpleGUI as sg

layout = [
    [sg.Text('Welcome losers, here are the solutions of the leetcode questions you were finding.')],
    [sg.Button('Two sums', size=(15, 1), key='-TWS-'), sg.Button('Palindrom Number', size=(15, 1), key=('-PAL-'))],
    [sg.Button('Longest Common prefix', size=(15, 1), key='-LCP-'),
     sg.Button('Valid Parentheses', size=(15, 1), key=('-VAL-'))],
    [sg.Exit()]
]

window = sg.Window('Solutions of ', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Exit':
        break

    if event == '-TWS-':
        sg.popup('''
        def two_sums(nums, target):
             dic = {}
             for index, values in enumerate(nums):
                 if target - values in dic:
                    return dic[target - values], index

                 else:
                    dic[values] = index
                    ''')
    if event == '-PAL-':
        sg.popup('''
        def Palindrom_str(x):
           s = x
           p = str(s)
           q = p[::-1]
           if q == p:
             return True
           else:
             return False


        def Palindrom_int(x):
           s = x
           a = 0
           while x > 0:
             r = x % 10
             x = x //10
             a = a*10 + r
           if a == s:
             return True
           else:
             return False

        ''')
    if event == '-LCP-':
        sg.popup('''
                def longestCommonPrefix(a):
                  size = len(a)

                # if size is 0, return empty string
                if (size == 0):
                    return ""

                if (size == 1):
                    return a[0]

                # sort the array of strings
                a.sort()

                # find the minimum length from
                # first and last string
                end = min(len(a[0]), len(a[size - 1]))

                # find the common prefix between
                # the first and last string
                i = 0
                while (i < end and
                a[0][i] == a[size - 1][i]):
                i += 1

                pre = a[0][0: i]
                return pre
                ''')

        if event == '-VAL-':
            sg.popup("""
               def valid_paretheses(strs):

                   open_brackets = ['(', '[', '{']
                   close_bracket = [')', ']', '}']
                   stack = []

                   for i in strs:
                       if i in open_brackets:
                            stack.append(i)

                       if i in close_bracket:
                            pos = close_bracket.index(i)

                            if 


                   """)

window.close()