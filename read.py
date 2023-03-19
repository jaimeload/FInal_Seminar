def read_phonebook():
    with open('Phonebook.txt', 'r') as f:
        phonebook = f.readlines()
        # print(phonebook)
    return phonebook