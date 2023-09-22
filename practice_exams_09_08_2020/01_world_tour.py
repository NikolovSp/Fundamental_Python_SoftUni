all_stops = input()
command = input()

while command != "Travel":

    command = command.split(':')

    if command[0] == "Add Stop":
        index = int(command[1])
        current_stop = command[2]
        if 0 <= index <= len(all_stops):
            all_stops = all_stops[:index] + current_stop + all_stops[index:]
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(all_stops) and 0 <= end_index <= len(all_stops):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
    else:
        old_string = command[1]
        new_string = command[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)

    print(all_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {all_stops}")
