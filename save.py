from read import read_phonebook

def save_phonebook(phonebook):
    with open('Phonebook.txt', 'w', encoding='utf-8') as f:
        for line in phonebook:
            f.write(line)