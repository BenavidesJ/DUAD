import re
import os
from models import Student

def is_number(input_value):
    if re.fullmatch(r'\d+', input_value):
        return True
    return False


def is_valid_grade(input_value):
    try:   
        if 0 <= int(input_value) <= 100:
            return True
        else:
            return False
    except ValueError:

        return False


def get_single_student_avg(student):
    return student.calculate_grades_avg()


def format_data(data):
    converted_data = []
    for item in data:
        grades = [
            {'Materia': 'Español', 'Nota': int(item.get('Nota Español'))},
            {'Materia': 'Inglés', 'Nota': int(item.get('Nota Inglés'))},
            {'Materia': 'Matemática', 'Nota': int(item.get('Nota Matemática'))},
            {'Materia': 'Ciencias', 'Nota': int(item.get('Nota Ciencias'))}
        ]
        name = item.get('Nombre')
        section = item.get('Seccion')
        student = Student(name, section, grades)
        
        converted_data.append(student)

    return converted_data


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
        
def display_students(students):
    for student in students:
        student.to_string()