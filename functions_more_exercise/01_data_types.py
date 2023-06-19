data = input()
if data == 'int':
    result = int(input()) * 2
elif data == 'real':
    result = f'{(float(input()) * 1.5):.2f}'
else:
    result = f'${input()}$'
print(result)
