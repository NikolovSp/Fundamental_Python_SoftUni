#3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards

materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_item = ''
materials_input = input().split()
for i in range(0, len(materials_input), 2):

    quantity = int(materials_input[i])
    material = materials_input[i + 1].lower()
    if material not in materials_dict:
        materials_dict[material] = quantity
    else:
        materials_dict[material] += quantity

    if 'shards' in materials_dict.keys() and materials_dict['shards'] >= 250:
        legendary_item = f'Shadowmourne obtained!'
        materials_dict['shards'] -= 250
        break
    elif "fragments" in materials_dict.keys() and materials_dict['fragments'] >= 250:
        legendary_item = f'Valanyr obtained!'
        materials_dict['fragments'] -= 250
        break
    elif 'motes' in materials_dict.keys() and materials_dict['motes'] >= 250:
        legendary_item = f'Dragonwrath obtained!'
        materials_dict['motes'] -= 250
        break

output = f"{legendary_item}\nshards: {materials_dict['shards']}\nfragments: {materials_dict['fragments']}\nmotes: {materials_dict['motes']}\n"
materials_dict.pop('shards')
materials_dict.pop('fragments')
materials_dict.pop('motes')
print(output, end="")
for k, v in materials_dict.items():
    print(f'{k}: {v}')

# print(materials_dict)
