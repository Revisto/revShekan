import random
import json

dict_file = open('my_secret_dictionary.json')
my_dict = json.load(dict_file)

def decrypt(text):
    text = text.split(" ")
    decrypted_text = ""
    for word in text:
        for key in my_dict:
            if word in my_dict[key]:
                decrypted_text += key

    return decrypted_text
