numbers_string = input()
#list_numbers = int().split()
string_list = (numbers_string.split())
# int_list = [int(x) for x in string_list]
int_list =[]
for x in string_list:
    int_list.append(int(x))

opposite_list = []
for opposite in int_list:
    opposite_list.append(opposite * -1)

print(opposite_list)
#longest solution
