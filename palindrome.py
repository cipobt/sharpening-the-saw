def is_palindrome(word):
    cleaned_word = ''.join(e.lower() for e in word if e.isalnum())
    return cleaned_word == cleaned_word[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
