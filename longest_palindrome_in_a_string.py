# Python program to find the longest
# palindromic substring.

# Function to find the longest palindrome substring
def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    start, maxLen = 0, 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for sub-string of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            if maxLen < 2:
                start = i
                maxLen = 2

    # Check for lengths greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1

            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True

                if k > maxLen:
                    start = i
                    maxLen = k

    return s[start:start + maxLen]

if __name__ == "__main__":
    s = "aaaabbaa"
    print(longestPalindrome(s))