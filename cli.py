while True:

    user_input = input(""" Hello there, this is a TEXT-Encryption & Decryption system made for bad days in Iran. (@revisto)
!!ONLY WOKS WITH PERSIAN LETTERS ONLY!!
What do you want to do?
1. Encrypt a message
2. Decrypt a message
3. Generate a secret dictionary 
Your Choice: """)


    if user_input == "1":
        user_input_text = input("Ok, Now please type your message. \n Input: ")
        from encryptor import encrypt
        print(encrypt(user_input_text))
        break

    elif user_input == "2":
        user_input_text = input("Ok, Now please type your encrypted message. \n Input: ")
        from decryptor import decrypt
        print(decrypt(user_input_text))
        break

    elif user_input == "3":
        from generator import generator
        print(generator())
        break

    else: 
        print("Your is not valid, retry...\n")