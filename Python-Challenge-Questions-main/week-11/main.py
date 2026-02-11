from student import Student

student1 = Student("Ceng", "12345", "Ada", 4, 3.7, "yes")

print(student1.print_information())
student1.predict_future_salary(1)

print("Enter information of second student: ")

department = input("Department: ").title()
ID = input("Student ID: ")
name = input("Name: ").title()
year = int(input("Years of study: "))
gpa = float(input("GPA: "))
scholarship = input("Scholarship(Yes/No):").lower()

student2 = Student(department, ID, name, year, gpa, scholarship)
print(student2.print_information())
student2.predict_future_salary(2)
