import random
import json

matched_words_count = 1
matched_words_for_space_count = 20
farsi_letters = "ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوژ"
english_letters = 'qwertyuiopasdfghjklzxcvbnm' #for future


words_file = open('words.json')
words = json.load(words_file)
my_dictionary = dict()

def generator():

    for first_letter in farsi_letters:
        for second_letter in farsi_letters:
            for third_letter in farsi_letters:
                chosen_words = []
                for i in range(matched_words_count):
                    chosen_words.append(random.choice(words))
                    words.remove(chosen_words[-1])
                my_dictionary[f"{first_letter}{second_letter}{third_letter}"] = chosen_words
        print(len(my_dictionary))

    for first_letter in farsi_letters:
        for second_letter in farsi_letters:
            chosen_words = []
            for i in range(matched_words_count):
                chosen_words.append(random.choice(words))
                words.remove(chosen_words[-1])
            my_dictionary[f"{first_letter}{second_letter}"] = chosen_words
                

    for first_letter in farsi_letters:
        chosen_words = []
        for i in range(matched_words_count):
            chosen_words.append(random.choice(words))
            words.remove(chosen_words[-1])
        my_dictionary[first_letter] = chosen_words


    chosen_words = []
    for i in range(matched_words_for_space_count):
            chosen_words.append(random.choice(words))
            words.remove(chosen_words[-1])
    my_dictionary[" "] = chosen_words


    with open('my_secret_dictionary.json', 'w') as fp:
        json.dump(my_dictionary, fp, ensure_ascii=False)

    return {"succuss": True, "path": "my_secret_dictionary.json"}