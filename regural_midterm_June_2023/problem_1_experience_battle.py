experience_needed = float(input())
battles = int(input())

success = False
counter = 0
for battle in range(1, battles + 1):
    experience_per_battle = float(input())
    counter += 1
    if battle % 3 == 0:
        experience_per_battle += (experience_per_battle * 0.15)

    if battle % 5 == 0:
        experience_per_battle -= (experience_per_battle * 0.10)

    if battle % 15 == 0:
        experience_per_battle += (experience_per_battle * 0.05)

    experience_needed -= experience_per_battle
    if experience_needed <= 0:
        success = True
        break

if success:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    print(f'Player was not able to collect the needed experience, {abs(experience_needed):.2f} more needed.')
