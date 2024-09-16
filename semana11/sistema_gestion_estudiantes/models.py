class Student():
    
    subjects_enrolled = ['Español', 'Inglés', 'Matemática', 'Ciencias']
    
    def __init__(self, name, section, grades):
        self.name = name
        self.section = section
        self.grades = grades
        
        
    def calculate_grades_avg(self):
        calc = 0
        for grade in self.grades:
            calc += grade["Nota"]
            average = calc / len(self.grades)
        return average
    


    def format_student_to_csv(self):
        grades = {grade['Materia']: grade['Nota'] for grade in self.grades}
        row_data = {
            'Nombre': self.name,
            'Seccion': self.section,
            f'Nota {self.subjects_enrolled[0]}': grades.get(self.subjects_enrolled[0]),
            f'Nota {self.subjects_enrolled[1]}': grades.get(self.subjects_enrolled[1]),
            f'Nota {self.subjects_enrolled[2]}': grades.get(self.subjects_enrolled[2]),
            f'Nota {self.subjects_enrolled[3]}': grades.get(self.subjects_enrolled[3]),
            'Promedio': self.calculate_grades_avg()
        }
        return row_data
     
        
    def to_string(self):
        print(f"Nombre: {self.name}")
        print(f"Seccion: {self.section}")
        
        for grade in self.grades:
            print(f"Nota de {grade["Materia"]}: {grade["Nota"]}")
        
        print(f"Promedio: {self.calculate_grades_avg()}")
        print('----------------------------------')