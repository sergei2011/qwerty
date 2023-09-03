def is_palindrome(word):
    count = 0
    word = (word.lower()).replace(" ", "")
    reversed_str = word[::-1]
    for item in range(len(word)):
        if word[item] == reversed_str[item]:
            count += 1

    if count == len(word):
        return True

    else:
        return False


print(is_palindrome(input()))