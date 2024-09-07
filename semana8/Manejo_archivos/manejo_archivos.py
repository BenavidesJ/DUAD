# Cree un programa que lea nombres de canciones de un archivo 
# (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
"""Funcion para ordenar una lista de canciones
    params: songs_list --> list: archivo leido y convertido a lista
    return: sorted_songs_list --> list: nueva lista ordenada
"""
def sort_songs(songs_list):
    sorted_songs_list = sorted(songs_list)
    return sorted_songs_list


"""Funcion para escribir archivo de lista de canciones ordenadas
    params: path --> string: path del archivo, list: sorted_data --> lista ordenada de canciones
    return: void, error
"""
def write_sorted_song_file(path, sorted_data):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            if( len(sorted_data) > 0):
                for line in sorted_data:
                    file.write(str(line))
            else:
                return
    except Exception as e:
        print(f'Se produjo un error: {e}')

    
"""Funcion para abrir un archivo de canciones
    params: string --> path: path del archivo
    return: list, error
"""        
def open_song_file(path):
    try:
        with open(path) as file:
            file_data = file.readlines()
            return sort_songs(file_data)
    except Exception as e:
        print(f'Se produjo un error: {e}')
        
        
"""Metodo main
    params: NO
    return: NO
"""        
def main():
    try:
        extension = '.txt'
        
        original_file_path = 'Manejo_archivos/canciones'
        
        new_file_path = f'{original_file_path}_ordenado'
        
        sorted_data_file = open_song_file(original_file_path + extension)
        write_sorted_song_file(new_file_path + extension, sorted_data_file)
    except Exception as e:
        print(f'Se produjo un error al ejecutar el programa\n {e}')

if __name__ == '__main__':
	main()