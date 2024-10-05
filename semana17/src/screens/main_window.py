import PySimpleGUI as sg
from src.screens.income_window import income_window
from src.screens.outcome_window import outcome_window
from src.screens.category_handler_window import category_handler_window
from src.utils.initial_loading import initial_loading
from src.account_movements.update_screen_data import update_screen_data
from common.strings import FILE_PATH, MAIN_WINDOW_NAME, ADD_INCOME, ADD_OUTCOME, ADD_CAT, CLEAN, TABLE_COL_NAMES

def main_window():
    movements = initial_loading(FILE_PATH)
        
    categories = list(set([mov['category'] for mov in movements]))
    
    layout = [  [sg.Text("Tabla de Ingresos y Gastos", font=("Arial", 20), text_color="#000000")],
                [sg.Text("Balance Total:", font=("Arial", 18), text_color="#000000"), sg.Text("0", key='account_balance', font=("Arial", 18), text_color="#000000" )],
                [sg.Table(
                    values=[],
                    headings=TABLE_COL_NAMES,
                    auto_size_columns=False,
                    col_widths=[10, 10, 20, 15],
                    key='tabla_datos',
                    num_rows=10,
                    justification='center'
                )],
                [sg.Button(ADD_INCOME), sg.Button(ADD_OUTCOME), sg.Button(ADD_CAT), sg.Button(CLEAN)] ]

    window = sg.Window(MAIN_WINDOW_NAME, layout, finalize=True)
    
    if len(movements):
        update_screen_data(window, movements)

    while True:
        event, values = window.read()
        
        if event == ADD_INCOME:
            income_window(movements, categories)
            update_screen_data(window, movements, write=True)
            
        if event == ADD_OUTCOME:
            outcome_window(movements, categories)
            update_screen_data(window, movements, write=True)
            
        if event == ADD_CAT:
            category_handler_window(categories)
            
        if event == CLEAN:
            update_screen_data(window, [], write=True)
            
        if event == sg.WIN_CLOSED:
            break
        

    window.close()