# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"

def is_palindrome(word):
    cleaned_word = ''.join(e.lower() for e in word if e.isalnum())
    return cleaned_word == cleaned_word[::-1]

def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

def reverse_string(s):
    return s[::-1]

def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def word_lengths(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

def count_character(string, char):
    return string.lower().count(char.lower())

def convert_to_title_case(string):
    return string.title()

def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

# Main menu function with options for different tasks
def main_menu():
    while True:
        print(f"\n{BLUE}String Manipulation Program{RESET}")
        print(f"{YELLOW}1. Check if a string is a palindrome{RESET}")
        print(f"{YELLOW}2. Count vowels in a string{RESET}")
        print(f"{YELLOW}3. Reverse a string{RESET}")
        print(f"{YELLOW}4. Check if two words are anagrams{RESET}")
        print(f"{YELLOW}5. Count occurrences of a character in a string{RESET}")
        print(f"{YELLOW}6. Find the length of each word in a sentence{RESET}")
        print(f"{YELLOW}7. Convert a string to title case{RESET}")
        print(f"{YELLOW}8. Find the length of the longest word in a sentence{RESET}")
        print(f"{YELLOW}9. Exit{RESET}")

        choice = input(f"{BLUE}Choose an option (1-9): {RESET}")

        if choice == '1':
            word = input("Enter a word or phrase: ")
            if is_palindrome(word):
                print(f"{GREEN}'{word}' is a palindrome!{RESET}")
            else:
                print(f"{RED}'{word}' is not a palindrome.{RESET}")

        elif choice == '2':
            user_string = input("Enter a string: ")
            print(f"Number of vowels: {count_vowels(user_string)}")

        elif choice == '3':
            user_string = input("Enter a string: ")
            print(f"Reversed string: {reverse_string(user_string)}")

        elif choice == '4':
            word1 = input("Enter the first word: ")
            word2 = input("Enter the second word: ")
            if are_anagrams(word1, word2):
                print(f"{GREEN}'{word1}' and '{word2}' are anagrams.{RESET}")
            else:
                print(f"{RED}'{word1}' and '{word2}' are not anagrams.{RESET}")

        elif choice == '5':
            user_input = input("Enter a string: ")
            character = input("Enter a character to count: ")
            if len(character) != 1:
                print(f"{RED}Please enter a single character.{RESET}")
            else:
                print(f"'{character}' appears {count_character(user_input, character)} time(s) in the string.")

        elif choice == '6':
            user_input = input("Enter a sentence: ")
            lengths = word_lengths(user_input)
            for word, length in lengths.items():
                print(f"'{word}' is {length} characters long.")

        elif choice == '7':
            user_input = input("Enter a string: ")
            print(f"Title case: {convert_to_title_case(user_input)}")

        elif choice == '8':
            sentence = input("Enter a sentence: ")
            print(f"The length of the longest word is: {longest_word_length(sentence)}")

        elif choice == '9':
            print(f"{GREEN}Exiting the program. Goodbye!{RESET}")
            break

        else:
            print(f"{RED}Invalid choice. Please select a valid option from the menu.{RESET}")

# Run the main menu
if __name__ == "__main__":
    main_menu()
