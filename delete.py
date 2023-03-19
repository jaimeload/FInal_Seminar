def delete_phonebook(search_term):
    phonebook = read_phonebook()
    with open('Phonebook.txt', 'w') as f:
        for line in phonebook:
            if search_term not in line:
                f.write(line)