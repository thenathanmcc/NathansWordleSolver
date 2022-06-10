#!/bin/env python3

# DB Connection Parameters
DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = "5432"
DATABASE_USER = "test"
DATABASE_USER_PASSWORD = "test_password"
DATABASE_NAME = "dictionary_db"

def permutations(curr_string, length, alphabet, index, weird_letters, important_letters):
    curr_letter = alphabet[index]
    letter_count = count_letters(curr_string,curr_letter)
    if letter_count >= 2:
        return
    if index == len(alphabet) - 1:
        return
    elif len(curr_string) == length:
        if has_import_letters(curr_string, important_letters) and curr_string[0] == 'r' and curr_string[1] == 'a' and curr_string[3] == 't':
            print(curr_string)
        return
    else:
        for letter in alphabet:
            permutations(curr_string + letter, length, alphabet, index+1, weird_letters, important_letters)

def count_letters(string, letter):
    count = 0
    for i in range(len(string)):
        if string[i] == letter:
            count += 1
    return count

def has_import_letters(string, letters):
    for letter in letters:
        if letter not in string:
            return False
    return True

alphabet = 'qwrtyuiopaghjzxvbm'
weird_letters = ['w', 'f', 'g', 'h', 'k', 'b', 'j', 'r']
important_letters = 'rat'
permutations('', 5, alphabet, 0, weird_letters, important_letters)