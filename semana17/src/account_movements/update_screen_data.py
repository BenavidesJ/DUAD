from src.utils.write_csv_file import write_csv_file
from src.account_movements.update_balance import actualizar_balance
from common.strings import FILE_PATH

def update_screen_data(window, movements, write=False) -> None:
    row_colors = []
    table_data = [[mov['type'], mov['amount'], mov['category'], mov['title']] for mov in movements]
    window['tabla_datos'].update(values=table_data)
    
    for i, mov in enumerate(movements):
        if mov['type'] == 'ingreso':
            row_colors.append((i,'#000000', '#A8E6A3'))
        elif mov['type'] == 'gasto':
            row_colors.append((i, '#FFFFFF','#FF6F61'))
    
    window['tabla_datos'].update(row_colors=row_colors)
    
    if(write):
        write_csv_file(FILE_PATH, movements, ("type", "amount", "title", "category"))
        
    balance = actualizar_balance(movements)
    window['account_balance'].update(f"{balance:.2f}")