def shuffle(s, t):
    if s == '':
        return [t]
    if t == '':
        return [s]
    else:
        a = s[1:]
        list1 = shuffle(a, t)
        for i in range(0, len(list1)):
            list1[i] = s[0] + list1[i]
        b = t[1:]
        list2 = shuffle(b, s)
        for i in range(0, len(list2)):
            list2[i] = t[0] + list2[i]
        tot_list = list1 + list2
        tot_set = list(set(tot_list))
        return tot_set
        



print(sorted(shuffle('', 'e')))
print()
print(sorted(shuffle('ab', 'cd')))
print(sorted(shuffle('abab', 'baba')))
