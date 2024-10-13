import csv
import os
from utils import format_data

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
    except Exception as e:
        print(f'Se presento un error abriendo el archivo requerido. error: {e}')
        return []
 
       
def write_csv_file(file_path, data, headers):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
        
        print('Los datos se guardaron correctamente!')
    except Exception as e:
        print(f'Se presento un error al intentar escribir en el archivo csc. error: {e}')

    
def initial_loading(file_path):
    try:
        if os.path.exists(file_path) and file_path.endswith('.csv'):
            reader = read_csv_file(file_path)
            data = format_data(reader)
            return data
        else:
            students_list = []
            return students_list
    except Exception as e:
        print(f'Se presento un error en la carga inicial de datos error: {e}')