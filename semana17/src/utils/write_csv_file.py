import PySimpleGUI as sg
import csv

def write_csv_file(file_path, data, headers):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
        
        sg.popup('Los datos se actualizaron correctamente!')
    except Exception as e:
        sg.popup(f'Se presento un error al intentar escribir en el archivo csc. error: {e}')