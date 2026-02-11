size = int(input("Enter the class size: "))
if size == 0:
    size += 1
sum_of_grades = 0
failed = 0
for i in range(size):
    grade = int(input(f"Enter the grade between 0 and 100 for student {i + 1}: "))

    if 0 <= grade <= 100:
        sum_of_grades += grade

    else:
        grade = int(input("Grade is out of range, please enter again: "))
        sum_of_grades += grade

    if 0 <= grade < 50:
        failed += 1

avg = sum_of_grades / size
print(f"Average of the grades is {avg}")
print(f"Number of students who failed is {failed}")
