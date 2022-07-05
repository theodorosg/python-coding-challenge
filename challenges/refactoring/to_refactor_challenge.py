def main_function_to_refactor():
    duplicates = create_duplicate_dictionary(removed_new_lines(read_file()))
    v = find_most_duplicated_value(duplicates)
    k = find_most_duplicated_key(duplicates)
    print(f"Most duplicated value(s): {k} and appeared {v} time(s)")
    print("Number of digits: ",find_number_of_digits(removed_new_lines(read_file())))
    print("Number of strings: ",find_number_of_letters(removed_new_lines(read_file())))
    print("Number of alphanumerics: ",find_number_of_alphanumerics(removed_new_lines(read_file())))


def read_file():
    f = open("/usr/src/app/challenges/refactoring/dictionary.txt", "r")
    l = []
    for i in range(0, 7):
        l.insert(i, f.readline())

    return l


def removed_new_lines(input):
    for i in range(0, 7):
        input[i] = input[i].strip()

    return input


def create_duplicate_dictionary(lst):
    r = {}

    for i in lst:
        r[i] = lst.count(i)

    return r


def find_most_duplicated_value(dict):
    most_duplicated_number = -1

    for k, v in dict.items():
        if v > most_duplicated_number:
            most_duplicated_number = v

    return most_duplicated_number


def find_most_duplicated_key(dict):
    most_duplicated_number = -1
    most_duplicated_value = ""
    for k, v in dict.items():
        if v > most_duplicated_number:
            most_duplicated_number = v
            most_duplicated_value = k

    return most_duplicated_value


def find_number_of_digits(l):
    c = 0
    for i in l:
        if i.isdigit():
            c += 1

    return c


def find_number_of_letters(l):
    c = 0
    for i in l:
        if i.isalpha():
            c += 1

    return c


def find_number_of_alphanumerics(l):
    c = 0
    for i in l:
        if i.isalnum():
            c += 1

    return c
