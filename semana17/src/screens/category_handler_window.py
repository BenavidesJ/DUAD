import PySimpleGUI as sg
from common.strings import ADD, CANCEL, CATEGORY_WINDOW_NAME, EXISTING_CATEGORY

def category_handler_window(categories):
    layout = [
        [sg.Text("Categoria")],
        [sg.Input(key='category')],
        [sg.Button(ADD), sg.Button(CANCEL)]
    ]

    window = sg.Window(CATEGORY_WINDOW_NAME, layout)

    while True:
        event, values = window.read()
        
        if event == ADD:
            category = values['category']
            if category not in categories:
                categories.append(category.lower())
                sg.popup(f"Categoria {category} agregada con exito!")
                break
            else:
                sg.popup(EXISTING_CATEGORY)

        if event == sg.WIN_CLOSED or event == CANCEL:
            break
        

    window.close()