def read_phonebook():
    with open('Phonebook.txt', 'r', encoding="utf-8") as f:
        phonebook = f.readlines()
        # print(phonebook)
    return phonebook