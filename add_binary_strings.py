def addBinary(s1, s2):
    # code here
    n, m = len(s1), len(s2)
    max_len = max(n, m) + 1
    resS = ['0'] * max_len
    i = n - 1
    j = m - 1
    k = len(resS) - 1
    carry = '0'
    while i >= 0 or j >= 0:
        if i >= 0:
            bit1 = s1[i]
            i -= 1
        else:
            bit1 = '0'
        if j >= 0:
            bit2 = s2[j]
            j -= 1
        else:
            bit2 = '0'
        if bit1 == '0' and bit2 == '0':
            resS[k] = carry
            carry = '0'
            k -= 1
            continue
        if (bit1 == '0' and bit2 == '1') or (bit1 == '1' and bit2 == '0'):
            if carry == '0':
                resS[k] = '1'
                k -= 1
                continue
            if carry == '1':
                resS[k] = '0'
                k -= 1
                continue
        if bit1 == '1' and bit2 == '1':
            if carry == '1':
                resS[k] = '1'
                k -= 1
                continue
            if carry == '0':
                resS[k] = '0'
                k -= 1
                carry = '1'
    resS[k] = carry
    finalString = ''
    for i in range(len(resS)):
        if resS[i] == '0':
            continue
        else:
            finalString = ''.join(resS[i:])
            break
    return finalString
print(addBinary('01001001', '0110101'))