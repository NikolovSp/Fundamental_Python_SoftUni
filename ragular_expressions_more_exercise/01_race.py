import re

pattern_letters = r'[A-Za-z]'
pattern_distance = r'\d'
participants = input().split(', ')
# print(participants)
sentence = input()

racers_dict = {}
while sentence != 'end of race':
    current_name = re.findall(pattern_letters, sentence)
    current_name = ''.join(current_name)
    current_distance = re.findall(pattern_distance, sentence)
    current_distance = [int(distance) for distance in current_distance]
    current_distance = sum(current_distance)

    if current_name in participants:
        if current_name not in racers_dict.keys():
            racers_dict[current_name] = current_distance
        else:
            racers_dict[current_name] += current_distance

    sentence = input()

sorted_racers = sorted(racers_dict.items(), key=lambda x: -x[1])
# print(sorted_racers)
print(f'1st place: {sorted_racers[0][0]}')
print(f'2nd place: {sorted_racers[1][0]}')
print(f'3rd place: {sorted_racers[2][0]}')

# import re
#
# def modify_dict(dict, name, result):
#     if name not in dict:
#         dict[name] = result
#     else:
#         dict[name] += result
#     return dict
#
#
# pattern_word = r'[A-Za-z]'
# pattern_digit = r'\d'
#
# list_name = input().split(", ")
# results_dict = {}
#
# while True:
#     code = input()
#     name = ""
#     distance = 0
#
#     if code == "end of race":
#         break
#     word_list = re.findall(pattern_word, code)
#     digit_list = re.findall(pattern_digit, code)
#
#     for i in range(len(digit_list)):
#         distance += int(digit_list[i])
#
#     for i in range(len(word_list)):
#         name += word_list[i]
#
#     if name in list_name:
#         results_dict = modify_dict(results_dict, name, distance)
#
# count = 0
# sorted_dict = dict(sorted(results_dict.items(), key=lambda x: x[1], reverse=True))
#
# for key in sorted_dict:
#     count += 1
#     if count > 3:
#         exit()
#     if count == 1:
#         print(f"{count}st place: {key}")
#     elif count == 2:
#         print(f"{count}nd place: {key}")
#     else:
#         print(f"{count}rd place: {key}")