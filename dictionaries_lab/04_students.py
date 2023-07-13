students = {}
lesson = ''

while True:
    student = input()

    if ':' not in student:
        if "_" in student:
            lesson = student.replace('_', ' ')
            break
        else:
            lesson = student
            break

    name, ID, course = student.split(':')
    if course not in students:
        students[course] = []
    students[course].append(f'{name} - {ID}')
# make a dictionary with key reppresenting the course - values - Name, ID. Then print only the values from dict with
# matching course name

print('\n'.join(students[lesson]))
