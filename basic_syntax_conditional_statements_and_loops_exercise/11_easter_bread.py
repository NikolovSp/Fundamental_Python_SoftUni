budget = float(input())
one_kg_flour_price = float(input())

one_pack_of_eggs_price = 0.75 * one_kg_flour_price
one_liter_milk_price = 1.25 * one_kg_flour_price * 0.25

bread_counter = 0
coloured_egg_counter = 0
price_for_one_bread = one_kg_flour_price + one_pack_of_eggs_price + one_liter_milk_price

while True:

    budget -= price_for_one_bread
    if budget < 0:
        budget += price_for_one_bread
        break

    bread_counter += 1
    coloured_egg_counter += 3

    if bread_counter % 3 == 0:
        coloured_egg_counter -= (bread_counter - 2)

print(f'You made {bread_counter} loaves of Easter bread! Now you have {coloured_egg_counter} eggs and'
      f' {budget:.2f}BGN left.')
