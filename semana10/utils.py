import re
import os
from common.constants import subjects

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


def calculate_average(grades):
    sum = 0
    for grade in grades:
        sum += grade["Nota"]
    average = sum / len(grades)
    return average


def get_single_student_avg(student):
    return student["Promedio"]


def format_data(data):
    converted_data = []
    for item in data:
        grades = [
            {'Materia': 'Español', 'Nota': int(item.get('Nota Español'))},
            {'Materia': 'Inglés', 'Nota': int(item.get('Nota Inglés'))},
            {'Materia': 'Matemática', 'Nota': int(item.get('Nota Matemática'))},
            {'Materia': 'Ciencias', 'Nota': int(item.get('Nota Ciencias'))}
        ]
        average = float(item.get('Promedio'))
        
        converted_data.append({
            'Nombre': item.get('Nombre'),
            'Seccion': item.get('Seccion'),
            'Notas': grades,
            'Promedio': average
        })

    return converted_data


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
        
def display_students(students):
    for student in students:
        print(f"Nombre: {student['Nombre']}")
        print(f"Seccion: {student['Seccion']}")
        
        subject_grades = {grade['Materia']: grade['Nota'] for grade in student['Notas']}
        
        for subject in subjects:
            print(f"Nota {subject}: {subject_grades.get(subject)}")
        print(f"Promedio de notas: {student['Promedio']}")
        print('----------------------------------')