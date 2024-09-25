import string
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    clean_string = remove_punctuation(user_input)
    print("String without punctuation:", clean_string)
