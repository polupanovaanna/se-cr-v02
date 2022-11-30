import random

import PySimpleGUI as sg
import app_cli

sg.theme('DarkPurple3')

layout = [
    [sg.Text('Player name'), sg.Input(key='-PLAYER_NAME-'), sg.Text('Bid'),
     sg.Combo(['VoisinsDeZero', 'Tier', 'Orphelins', 'Parity 1', 'Parity 0', 'Color R', 'Color G', 'Color B'], key='-PLAYER_BID-'),
     sg.Button('Add player')],
    [sg.Text('Diler name'), sg.Input(key='-DILER_NAME-'), sg.Button('Add diler')],
    [sg.Text('Players'), sg.Output(size=(30, 20), key='-OUTPUT-'),
     sg.Text('Results'), sg.Output(size=(30, 20), key='-RESULTS-')],
    [sg.Button('Start game'), sg.Button('Exit'), sg.Button('New game')]
]
window = sg.Window('File Compare', layout)
while True:
    # The Event Loop
    event, values = window.read()

    if event == 'Add player':
        app_cli.add_player(values['-PLAYER_NAME-'], values['-PLAYER_BID-'])
        playerlist = app_cli.get_player_list()
        window['-OUTPUT-'].update(playerlist)
    elif event == 'Add diler':
        app_cli.add_player(values['-DILER_NAME-'], random.choice(app_cli.possible_rates))
        playerlist = app_cli.get_player_list()
        window['-OUTPUT-'].update(playerlist)
    elif event == 'Start game':
        window['-RESULTS-'].update(app_cli.get_results())
    elif event == 'New game':
        app_cli.players.clear()
        window['-OUTPUT-'].update('')
        window['-RESULTS-'].update('')

    if event in (None, 'Exit'):
        break