resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity
# print(resources)

for key, value in resources.items():
    print(f"{key} -> {value}")
