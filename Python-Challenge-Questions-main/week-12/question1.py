courses = []
for i in range(3):
    course = input("Please enter three course name: ").upper()
    courses.append(course)

courses.sort()
courses.reverse()

result = ""
for course in courses:
    result += course

print(result)
