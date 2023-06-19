def is_palindrome(words):
    list_of_palindromes = []
    for word in words:
        if word == word[::-1]:
            list_of_palindromes.append(word)
    return list_of_palindromes


strings = input().split()
palindrome = input()
result = is_palindrome(strings)
palindrome_occurrence = result.count(palindrome)
print(result)
print(f'Found palindrome {palindrome_occurrence} times')
