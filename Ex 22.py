string1 = input().lower()
string2 = input().lower()

if sorted(string1) == sorted(string2):
    print("Are anagrams")
else:
    print("Are not anagrams")