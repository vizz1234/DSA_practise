def constructLPS(s):
    lps = [0] * len(s)
    lps[0] = 0
    lpsI = 0
    i = 1
    while i < len(s):
        if s[lpsI] == s[i]:
            lpsI += 1
            lps[i] = lpsI
            i += 1
        else:
            if lpsI == 0:
                lps[i] = 0
                i += 1
            else:
                lpsI = lps[lpsI - 1]
    return lps
def strings_rotation_of_each_other(s1, s2):
    if len(s1) != len(s2):
        return False
    lps = constructLPS(s2)
    s1 = s1 + s1
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == len(s2):
            return True
    return False

print(strings_rotation_of_each_other("AAB", "ABB"))