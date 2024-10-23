def capitalize_words(sentence):
    return sentence.title()

def string_length(s):
    return len(s)

def find_shortest_word(sentence):
    words = sentence.split()
    return min(words, key=len)


sentence = input("Enter a sentence: ")
print(f"Capitalized sentence: {capitalize_words(sentence)}")


user_input = input("Enter a string: ")
print(f"The length of the string is: {string_length(user_input)}")


sentence = input("Enter a sentence: ")
print(f"The shortest word is: '{find_shortest_word(sentence)}'")

