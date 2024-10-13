def actualizar_balance(movements):
    total_ingresos = sum([float(mov['amount']) for mov in movements if mov['type'] == 'ingreso'])
    total_gastos = sum([float(mov['amount']) for mov in movements if mov['type'] == 'gasto'])
    balance = total_ingresos - total_gastos
    return balance