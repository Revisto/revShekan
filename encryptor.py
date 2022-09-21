import random
import json

dict_file = open('my_secret_dictionary.json')
my_dict = json.load(dict_file)


def encrypt(text):
    text = text.split(" ")
    encrypted_text = ""
    for word in text:
        while word != "":
            if len(word) >= 3:
                splited_letters = word[0] + word[1] + word[2]
                encrypted_text += " " + random.choice(my_dict[splited_letters])
                word = word[3:]

            elif len(word) >= 2:
                splited_letters = word[0] + word[1]
                encrypted_text += " " + random.choice(my_dict[splited_letters])
                word = word[2:]

            else:
                splited_letters = word[0]
                encrypted_text += " " + random.choice(my_dict[splited_letters])
                word = word[1:]
        encrypted_text += " " + random.choice(my_dict[" "])

    return encrypted_text
