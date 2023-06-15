numbers = input()
string_list = numbers.split() #add strings to list
int_list = [int(x) for x in string_list] #coverts each value in list to int
opposite_list = [-x for x in int_list] #converts each value into opposite * -1
print(opposite_list)
