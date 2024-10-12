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

def word_lengths(words):
    return {word: len(word) for word in words}

user_input = input("Enter words separated by spaces: ").split()
lengths = word_lengths(user_input)

for word, length in lengths.items():
    print(f"'{word}' is {length} characters long.")



word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")


user_string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(user_string)}")


user_string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(user_string)}")


user_string = input("Enter a word or phrase: ")
if is_palindrome(user_string):
    print(f"'{user_string}' is a palindrome")
else:
    print(f"'{user_string}' is not a palindrome")
