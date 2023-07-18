number_of_grades = int(input())

grades_dict = {}
for _ in range(number_of_grades):
    name = input()
    grade = float(input())

    if name not in grades_dict.keys():
        grades_dict[name] = []
    grades_dict[name].append(grade)


for name, grade in grades_dict.items():
    average_grade = sum(grade) / len(grade)
    if (sum(grade) / len(grade)) >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
