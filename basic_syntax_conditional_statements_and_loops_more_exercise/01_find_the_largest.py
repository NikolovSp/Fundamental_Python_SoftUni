number = input()

largest_number = 0

for i in range(len(number)):
    number = int(number)

    digit = number % 10
    number = number // 10
#not sure how to compare all digits at the same time without a list?
