import PySimpleGUI as sg
import os
from .read_csv_file import read_csv_file

def initial_loading(file_path):
    try:
        if os.path.exists(file_path) and file_path.endswith('.csv'):
            data = read_csv_file(file_path)
            return data
        else:
            movements = []
            return movements
    except Exception as e:
        sg.popup(f'Se presento un error en la carga inicial de datos error: {e}')