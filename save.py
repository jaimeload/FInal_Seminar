def save_phonebook(phonebook):
    with open('Phonebook.txt', 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0)
        f.write(content)
        f.truncate()       