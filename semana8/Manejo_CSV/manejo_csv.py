import csv

def enter_data():
    name = input('Ingrese el nombre del videojuego\n')
    genre = input('Ingrese el genero del videojuego\n')
    dev_company = input('Ingrese la empresa que desarrollo el videojuego\n')
    esrb_qualification = input('Ingrese la calificacion ESRB\n')
    
    game_data_dictionary = {
        "ID": 0,
        "Nombre": name,
        "Genero": genre,
        "Desarrollador": dev_company,
        "Clasificacion": esrb_qualification
    }
    
    return game_data_dictionary


def manage_data(n):
    cont = 0
    data_list = []
    while cont < n:
        data_dictionary = enter_data()
        data_dictionary["ID"] = cont
        data_list.append(data_dictionary)
        cont += 1
    
    return data_list


def create_CSV_file(file_path, data, headers):
    try:
        with open(file_path, 'w', encoding='utf-8',newline='') as file:
            wrt = csv.DictWriter(file, headers)
            wrt.writeheader()
            wrt.writerows(data)
    except Exception as e:
        print(f'Hubo un error y no se pudo generar el archivo error: {e}')

       
def main():
    try:
        file_path = 'videogames.csv'
        
        quantity = int(input('Cuantos videojuegos desea agregar??'))
        
        data = manage_data(quantity)
        
        data_headers = data[0].keys()
        
        create_CSV_file(file_path, data, data_headers)
        
        print(f'El archivo {file_path} se ha creado exitosamente')
    except Exception as e:
        print(f'Hubo un error al ejecutar el programa {e}')
        
        
if __name__ == '__main__':
	main()