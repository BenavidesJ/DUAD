from utils import is_number, is_valid_grade, get_single_student_avg, display_students, format_data
from data import write_csv_file, read_csv_file, initial_loading
from common.constants import subjects
from models import Student

def add_students(students_list):
    repeat_cicle = 's'

    while repeat_cicle != 'n':
        grades = []
        
        name = input('Ingrese el nombre del estudiante\n')
        section = input('Ingrese la sección del estudiante\n')
        
        for sub in subjects:
            grade = input(f'Ingrese la nota de {sub}\n')
            
            while not(is_number(grade)) or not(is_valid_grade(grade)):
                print(f'Error: La nota para {sub} debe estar entre 0 y 100.')
                grade = input(f'Por favor ingrese nuevamente la nota de {sub} (0-100)\n')
            
            student_grades = {
                "Materia": sub,
                "Nota": int(grade)
            }
            
            grades.append(student_grades)
        
        student = Student(name, section, grades)
        
        students_list.append(student)
        
        repeat_cicle = input('¿Desea ingresar otro estudiante más? (s/n): ').lower()
        
        while repeat_cicle not in ['s', 'n']: 
            repeat_cicle = input('Esa no es una opción correcta. ¿Desea ingresar otro estudiante más? (s/n): ').lower()
    
    return students_list


def get_students(students_list):
    if not students_list:
        print('No hay estudiantes agregados!')
    else:
        display_students(students_list)
         
        
def get_top3_students(students_list):
    if students_list is not None:
        top_3_students = sorted(students_list, key=get_single_student_avg, reverse=True)
        display_students(top_3_students[:3])
    else:
        print("No hay datos para mostrar")
    
    
def get_total_students_average(students_list):
    add = 0
    for student in students_list:
        add += get_single_student_avg(student)
    all_scores_average = add / len(students_list)
    print(f'El promedio total de notas es {all_scores_average}')


def save_data_to_csv(path, students_data):
    headers = ('Nombre', 'Seccion', f'Nota {subjects[0]}', f'Nota {subjects[1]}', f'Nota {subjects[2]}', f'Nota {subjects[3]}', 'Promedio')
    try:
        formatted_data = []
        for student in students_data:
            formatted_data.append(student.format_student_to_csv())
        write_csv_file(path, formatted_data, headers)
    except Exception as e:
        print(f'Ocurrio un error salvado los datos error: {e}')
       
        
def load_data_from_csv(path):
    try:
        reader = read_csv_file(path)
        data = format_data(reader)
        return data
    except Exception as e:
        print(f'Ocurrio un error cargando los datos error: {e}')
        return []
    
def load_data_on_init(path):
    try:
        data = initial_loading(path)
        return data
    except Exception as e:
        print(f'Ocurrio un error cargando los datos error: {e}')
