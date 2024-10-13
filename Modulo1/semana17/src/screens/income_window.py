import PySimpleGUI as sg
from src.account_movements.add_movement import add_movement
from src.screens.category_handler_window import category_handler_window
from common.strings import NON_EXISTING_CATEGORY, INCOME_WINDOW_NAME, CANCEL, ADD, NON_VALID_AMOUNT, NON_VALID_FIELDS

def income_window(movements, categories):
    layout = [
        [sg.Text("Título o descripción del ingreso")],
        [sg.Input(key='income_title')],
        [sg.Text("Monto")],
        [sg.Input(key='amount', size=(10, 1))],
        [sg.Text("Categoría")],
        [sg.Input(key='category')],
        [sg.Button(ADD), sg.Button(CANCEL)]
    ]

    window = sg.Window(INCOME_WINDOW_NAME, layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == CANCEL:
            break

        if event == 'Agregar':
            description = values['income_title']
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

            income = add_movement('ingreso', amount, description, category)
            movements.append(income)
            sg.popup("Ingreso registrado exitosamente!")
            window.close()

    window.close()
