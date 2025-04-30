# Python code for Longest String Chain
# using DP + Hashing

def longestStringChain(words):
    # Sort words by length
    words.sort(key=len)
    
    # Dictionary to store the maximum chain length for each word
    dp = {}
    
    res = 1
    
    # Iterate through each word in the sorted list
    for w in words:
        dp[w] = 1  # Initialize length for current word
        
        # Try removing one character at a time
        for i in range(len(w)):
            pred = w[:i] + w[i+1:]
            if pred in dp:
                dp[w] = max(dp[w], dp[pred] + 1)
        
        res = max(res, dp[w])
    
    return res

# Driver code
if __name__ == "__main__":
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longestStringChain(words))