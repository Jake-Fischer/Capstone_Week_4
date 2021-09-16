
def camel_case(sentence):
    """ Convert sentence to camelCase, for example, "Display all books" is converted to "displayAllBooks"
        As of now, unable to handle apostrophies """
    if isinstance(sentence, str):
        title_case = sentence.title() # Uppercase first letter of each word
        upper_camel_cased = title_case.replace(' ', '').replace('\n', '').replace('\t','') # remove spaces, newlines, and tabs
        # Lowercase first letter, join with rest of string 
        # # Slices don't produce index out of bounds errors. 
        # # So this still works on empty strings, strings of length 1
        return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]
    else:
        return False


def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)

    if camelcased:
        print(camelcased)
    else:
        print('Something went very wrong, please restart the program and try again.')


if __name__ == '__main__':
    main()