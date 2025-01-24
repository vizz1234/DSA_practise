def implement_atoi(s):
    idx = 0
    sign = 1
    result = 0
    while idx < len(s) and s[idx] == " ":
        idx += 1
    if idx < len(s) and s[idx] == "-":
        sign = -1
        idx += 1
    while idx < len(s) and '0' <= s[idx] <= '9':
        result = result * 10 + (ord(s[idx]) - ord('0'))
        idx += 1
    if result > 2**31 - 1:
        return 2**31 - 1 if sign == 1 else -2**31
    return sign * result

print(implement_atoi("-123"))