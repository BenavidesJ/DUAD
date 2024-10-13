import PySimpleGUI as sg
from src.account_movements.add_movement import add_movement
from src.screens.category_handler_window import category_handler_window
from common.strings import OUTCOME_WINDOW_NAME, CANCEL, ADD, NON_EXISTING_CATEGORY, NON_VALID_AMOUNT, NON_VALID_FIELDS

def outcome_window(movements, categories):
    layout = [
        [sg.Text("Título o descripción del gasto")],
        [sg.Input(key='outcome_title')],
        [sg.Text("Monto")],
        [sg.Input(key='amount', size=(10, 1))],
        [sg.Text("Categoría")],
        [sg.Input(key='category')],
        [sg.Button(ADD), sg.Button(CANCEL)]
    ]

    window = sg.Window(OUTCOME_WINDOW_NAME, layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == CANCEL:
            break

        if event == ADD:
            description = values['outcome_title']
            category = values['category']
            if category.lower() not in categories:
                sg.popup(NON_EXISTING_CATEGORY)
                category_handler_window(categories)
                
            try:
                amount = float(values['amount'])
            except ValueError:
                sg.popup(NON_VALID_AMOUNT)
                continue

            if not description or not category:
                sg.popup(NON_VALID_FIELDS)
                continue

            outcome = add_movement('gasto', amount, description, category)
            movements.append(outcome)
            sg.popup("Gasto registrado exitosamente!")
            window.close()

    window.close()