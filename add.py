def add_phonebook(new_data):
    with open('Phonebook.txt', 'a') as f:
        f.write(new_data + '\n')