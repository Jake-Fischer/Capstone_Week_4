import re

sentence = "I'm a sentence"

sentence_title = sentence.title()

print(sentence)
print(sentence_title)

words = sentence.split(' ')
capitalized_word_list = []

for word in words:
    first_letter = word[0]
    capitalized_first_letter = first_letter.capitalize()
    word[0] = capitalized_first_letter 
    capitalized_word_list.append(word)


capitalized_sentence = capitalized_word_list.join('')

capitalized_sentence[0] = capitalized_sentence[0].lower()

print(capitalized_sentence)