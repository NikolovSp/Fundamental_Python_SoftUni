resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in resources.keys():
        resources[resource] = 0
    resources[resource] += quantity
# print(resources)

for key, value in resources.items():
    print(f"{key} -> {value}")
