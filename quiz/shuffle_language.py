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
        return tot_list

def shuffle_language(A, B):
    if len(A) == 0 and len(B) == 0:
        return []
    else:
        ultra_list = []
        for a in A:
            for b in B:
                ultra_list += shuffle(a, b)    
    gig_list = list(set(ultra_list))
    return gig_list

print(sorted(shuffle_language({'ab'}, {'cd', 'e'})))
print(sorted(shuffle_language({}, {'aa', 'ab', 'bb'})))
print(sorted(shuffle_language({'aba', 'baa', 'aab'}, {'aab', 'bba', 'aaa'})))