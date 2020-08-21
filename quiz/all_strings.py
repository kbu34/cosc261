def all_strings(alpha, length):
    if length == 0:
        return ['']
    else:
        pre_list = all_strings(alpha, length - 1)
        new_list = []
        for x in pre_list:
            for y in alpha:
                new_string = str(x) + str(y)
                new_list.append(new_string)
        return new_list
    
print(len(all_strings({'a', 'b', 'c'}, 2)))
print(sorted(all_strings({0, 1}, 3)))
print(sorted(all_strings({'a', 'b'}, 2)))