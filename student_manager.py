import json
import os
from student import Student

class StudentManager:

    FILE_NAME = "data.json"

    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME,"r") as file:
                    data = json.load(file)

                    for item in data:
                        student = Student(
                            item["student_id"],
                            item["name"],
                            item["age"],
                            item["course"]
                        )
                        self.students.append(student)
            except (json.JSONDecodeError, ValueError):
                # Handle empty or corrupted JSON file
                self.students = []

    def save_student(self):          

        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(self.FILE_NAME,"w") as file:
            json.dump(data,file,indent=4) 

    def add_student(self,student):
        self.students.append(student)
        self.save_student()

    def get_student(self):
        return self.students  
    
    def delete_students(self,student_id):

        self.students = [
            student
            for student in self.students
            if  student.student_id != student_id
        ]

        self.save_student()

    def search_student(self,student_id):

        for student in self.students:

            if student.student_id == student_id:
                return student
            
        return None    
    
    def update_student(self,student_id,name,age,course):

        student = self.search_student(student_id)

        if student:
            student.name = name
            student.age = age
            student.course = course

            self.save_student()
            return True
        
        return False














