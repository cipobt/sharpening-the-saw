def capitalize_words(sentence):
    return sentence.title()

def string_length(s):
    return len(s)



sentence = input("Enter a sentence: ")
print(f"Capitalized sentence: {capitalize_words(sentence)}")


user_input = input("Enter a string: ")
print(f"The length of the string is: {string_length(user_input)}")

