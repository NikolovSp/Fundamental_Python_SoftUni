people = list(map(int, input().split()))
k = int(input())
# print(people)
executed_list = []
counter = 0
index = 0
while len(people) > 0:
    counter += 1
    if counter % k == 0:
        current_kill = people[index]
        executed_list.append(current_kill)
        people.remove(current_kill)
    else:
        index += 1

    if index >= len(people):
        index = 0

# print(executed_list)
print('[',end='')
for i in range(len(executed_list)):
    print(f'{executed_list[i]},',end='')
print(f']')
