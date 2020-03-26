string = input('string: ')

new_string = ''
for char in string:
    char_code = ord(char)
    if char_code in range(97, 123):
        if not (char_code + 2) in range(97, 123):
            new_char_code = char_code + 2 - 26
        else:
            new_char_code = char_code + 2
        new_string = new_string + chr(new_char_code)
    else:
        new_string = new_string + char

print(new_string)

trans_dict = {'a': 99, 'b': 100}
print(string.maketrans(trans_dict))
