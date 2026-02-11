class Student:

    def __init__(self, department, student_id, name, year_of_study, gpa, has_scholarship):
        self.department = department
        self.id = student_id
        self.name = name
        self.year = year_of_study
        self.gpa = gpa
        if has_scholarship == "yes":
            self.scholarship = True
        else:
            self.scholarship = False

    def predict_future_salary(self, x):
        """" This method predicts the salary based on country"""
        if x == 1:
            turkey_salary = (self.gpa * 1000) - (self.year * 10)
            if self.scholarship:
                turkey_salary += 300
            print(f"This student may get {turkey_salary} TL as salary in Turkey.")
        elif x == 2:
            abroad_salary = (self.gpa * 10000) - (self.year * 100)
            if self.scholarship:
                abroad_salary += 2000
            print(f"This student may get {abroad_salary} TL as salary in abroad.")
        else:
            print("Invalid input!")

    def print_information(self):
        if self.scholarship:
            return f'{self.name}, whose student ID is {self.id}, is studying {self.year}th year  at the "{self.department}" department with scholarship. {self.name} has a GPA of {self.gpa}.'
        else:
            return f'{self.name}, whose student ID is {self.id}, is studying {self.year}th year  at the "{self.department}" department without scholarship. {self.name} has a GPA of {self.gpa}.'
