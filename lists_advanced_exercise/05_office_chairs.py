def chair_count(num):
    free_chairs = 0
    game_on = True
    for room in range(1, num + 1):
        chairs = input().split()
        if len(chairs[0]) >= int(chairs[1]):
            free_chairs += len(chairs[0]) - int(chairs[1])
        else:
            needed_charis = int(chairs[1]) - len(chairs[0])
            print(f'{needed_charis} more chairs needed in room {room}')
            game_on = False
    if game_on:
        print(f"Game On, {free_chairs} free chairs left")


rooms = int(input())
chair_count(rooms)
