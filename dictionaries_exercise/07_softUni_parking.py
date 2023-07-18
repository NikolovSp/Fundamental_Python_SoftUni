n = int(input())

parking_lot = {}
for _ in range(n):
    person = input().split()

    if person[0] == 'register':
        username = person[1]
        licence_plate = person[2]
        if username not in parking_lot.keys():
            parking_lot[username] = licence_plate
            print(f"{username} registered {licence_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {licence_plate}")

    elif person[0] == 'unregister':
        username = person[1]
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]

for username, licence_plate in parking_lot.items():
    print(f"{username} => {licence_plate}")
