def office_happiness():
    employees_happiness = list(map(int, input().split()))
    factor_happiness = int(input())

    factored_happiness = list(map(lambda x: x * factor_happiness, employees_happiness))
    average_happiness = sum(factored_happiness) / len(factored_happiness)
    happy_employees_counter = 0
    for happy in factored_happiness:
        if happy >= average_happiness:
            happy_employees_counter += 1

    if happy_employees_counter >= len(factored_happiness) / 2:
        result = f'Score: {happy_employees_counter}/{len(factored_happiness)}. Employees are happy!'
    else:
        result = f'Score: {happy_employees_counter}/{len(factored_happiness)}. Employees are not happy!'

    return result

result = office_happiness()
print(result)
