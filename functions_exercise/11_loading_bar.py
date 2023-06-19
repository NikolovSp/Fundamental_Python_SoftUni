def loading_bar(num):
    n = int(num / 10)
    if num == 100:
        return f'{num}% Complete! \n[{n * "%"}]'
    else:
        return f'{num}% [{n * "%"}{(10 - n) * "."}] \nStill loading...'


number = int(input())
print(loading_bar(number))
