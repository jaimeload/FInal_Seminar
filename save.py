def save_phonebook(phonebook):
    with open('Phonebook.txt', 'w') as f:
        for line in phonebook:
            f.write(line)