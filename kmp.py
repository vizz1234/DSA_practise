def constructLPS(pat):
    n = len(pat)
    lps = [0] * n 
    lps[0] = 0
    lpsI = 0
    i = 1
    while i < n:
        if pat[lpsI] == pat[i]:
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
        
def search(pat, txt):
    # code here
    lps = constructLPS(pat)
    res = []
    n = len(txt)
    m = len(pat)
    i = 0
    j = 0
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            
            if j == m:
                res.append(i-j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res
print(search(txt = 'geeksforgeeks', pat = 'geek'))