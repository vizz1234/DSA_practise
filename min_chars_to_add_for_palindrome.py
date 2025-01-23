def construct_lps(s):
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

def min_chars_to_add_for_palindrome(s):
    revS = s[::-1]
    lps = construct_lps(s + "$" + revS)
    return len(s) - lps[-1]

print(min_chars_to_add_for_palindrome("aacecaaaa"))