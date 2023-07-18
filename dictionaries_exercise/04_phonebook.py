phone_book = {}

while True:
    person = input()
    if '-' not in person:
        break

    name, phone = person.split('-')
    phone_book[name] = phone
# print(phone_book)
for i in range(int(person)):
    account_search = input()
    if account_search in phone_book.keys():
        print(f"{account_search} -> {phone_book[account_search]}")
    else:
        print(f"Contact {account_search} does not exist.")
