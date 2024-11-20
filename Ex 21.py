word = input()
reversed_word = word[::-1]

if word == reversed_word:
    print("Is a palindrome")
else:
    print("Is not a palindrome")