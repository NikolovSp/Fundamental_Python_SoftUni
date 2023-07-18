courses = {}

while True:
    students = input().split(' : ')

    if students[0] == 'end':
        break

    current_course = students[0]
    current_name = students[1]

    if current_course not in courses.keys():
        courses[current_course] = []
    courses[current_course].append(current_name)

for course in courses.keys():
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
