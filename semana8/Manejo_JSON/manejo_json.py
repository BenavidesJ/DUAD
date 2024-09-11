import json

def load_json_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            parsed_file = json.load(file)
            return parsed_file
    except FileNotFoundError:
        print(f"El archivo {file_name} no existe. Se creará uno nuevo.")
        return []
    except Exception as e:
        print(f'Hubo un error al intentar abrir el archivo {e}')


def create_new_pokemon():
    stat_points_dictionary = {}
    pokemon_types = []
    
    name = input('Cual es el nombre del pokemon que quiere agregar?\n')
    pokemon_types_quantity = int(input('Cuantos tipos tiene tu pokemon?\n'))
    for _ in range(pokemon_types_quantity):
        pokemon_type = input('Cual es el tipo del pokemon?\n')
        pokemon_types.append(pokemon_type)
        
    pokemon_stats = ['HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed']
    for stat in pokemon_stats:
        points = int(input(f'Cuantos puntos de {stat} tiene tu pokemon?\n'))
        stat_points_dictionary[stat] = points
        
    pokemon =  {
        "name": {
          "english": name
        },
        "type": pokemon_types,
        "base": stat_points_dictionary
    }
    
    return pokemon
    

def save_json_file(file_name, data):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f'El archivo {file_name} ha sido sobrescrito exitosamente. Un nuevo pokemon ha sido agregado!')
    except Exception as e:
        print(f'Hubo un error al intentar escribir en el archivo: {e}')


def main():
    try:
        file = 'pokemon.json'
        
        pokemon_data = load_json_file(file)
        
        pokemon = create_new_pokemon()
        
        pokemon_data.append(pokemon)
        
        save_json_file(file, pokemon_data)
    except Exception as e:
        print(f'Se produjo un error al ejecutar el programa\n {e}')
        
        
if __name__ == '__main__':
	main()