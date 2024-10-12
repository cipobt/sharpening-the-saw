def is_palindrome(word):
    cleaned_word = ''.join(e.lower() for e in word if e.isalnum())
    return cleaned_word == cleaned_word[::-1]

def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

# Reversing String function
def reverse_string(s):
    return s[::-1]

# Determining palindrome function
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")


user_string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(user_string)}")
