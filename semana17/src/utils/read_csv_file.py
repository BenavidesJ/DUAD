import PySimpleGUI as sg
import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
    except Exception as e:
        sg.popup(f'Se presento un error abriendo el archivo requerido. error: {e}')
        return []