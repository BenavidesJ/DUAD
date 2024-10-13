from actions import add_students, get_students, get_top3_students, get_total_students_average, save_data_to_csv, load_data_from_csv, load_data_on_init
from common.strings import menu_str, handled_data_file_path
from utils import clear_console

def wait_for_continue():
    input('\nPara continuar presione cualquier tecla...')
    clear_console()


def menu():
    
    students = load_data_on_init(handled_data_file_path)
    clear_console()
    option = input(menu_str)
    
    while int(option) != 0:
        if int(option) == 1:
            add_students(students)
            wait_for_continue()
            option = input(menu_str)
        elif int(option) == 2:
            get_students(students)
            wait_for_continue()
            option = input(menu_str)
        elif int(option) == 3:
            get_top3_students(students)
            wait_for_continue()
            option = input(menu_str)
        elif int(option) == 4:
            get_total_students_average(students)
            wait_for_continue()
            option = input(menu_str)
        elif int(option) == 5:
            save_data_to_csv(handled_data_file_path,students)
            wait_for_continue()
            option = input(menu_str)
        elif int(option) == 6:
            students = load_data_from_csv(handled_data_file_path)
            wait_for_continue()
            option = input(menu_str)
        else:
            print('Esa no es una opcion correcta')
            wait_for_continue()
            option = input(menu_str)