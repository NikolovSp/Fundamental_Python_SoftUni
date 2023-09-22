def is_valid_message(message):
    import re

    pattern = r'^([$%])([A-Z][a-z]{2,})\1:\s*(\[\d+\]\|\[\d+\]\|\[\d+\]\|)$'
    match = re.match(pattern, message)
    if match:
        return True
    else:
        return False


def decrypt_message(message):
    import re

    numbers_pattern = r'\[(\d+)\]'
    decrypted_nums = [chr(int(num)) for num in re.findall(numbers_pattern, message)]
    return ''.join(decrypted_nums)


def main():
    num_inputs = int(input())
    for _ in range(num_inputs):
        message = input()
        if is_valid_message(message):
            decrypted_message = decrypt_message(message)
            tag = message.split(':')[0]
            tag = tag[1:-2]
            print(f"{tag}: {decrypted_message}")
        else:
            print("Valid message not found!")


if __name__ == "__main__":
    main()
