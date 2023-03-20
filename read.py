def read_phonebook():
    import os
    current_directory = os.path.dirname(os.path.abspath('Phonebook.py'))
    phonebook_path = os.path.join(current_directory, 'Phonebook.txt')
    phonebook = []
    with open(phonebook_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            phonebook.append(str(i) + '   ' + line.strip())
    return phonebook