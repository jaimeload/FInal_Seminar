def fix_phone_number(phone_number):
    if phone_number.startswith('8'):
        phone_number = '+7' + phone_number[1:]
    elif not phone_number.startswith('+'):
        phone_number = '+' + phone_number
    return phone_number

def add_phonebook(family, name, patronymic, phone):
    with open('Phonebook.txt', 'a', encoding='utf-8') as f:
        family_width = 15
        name_width = 15
        patronymic_width = 15
        phone_width = 12
        phone = fix_phone_number(phone)
        new_line = family.ljust(family_width) + name.ljust(name_width) + patronymic.ljust(patronymic_width) + phone.ljust(phone_width)
        f.write('\n')
        f.write(new_line)