s = 'I_am_a_apple'
my_dict = {}
for letter in s:
    my_dict[letter] = my_dict.get(letter, 1)+1
print(my_dict)