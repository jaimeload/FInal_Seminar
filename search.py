from read import read_phonebook

def search_phonebook(search_term):
    phonebook = read_phonebook()
    results = []
    for line in phonebook:
        if search_term in line:
            results.append(line)
    return results