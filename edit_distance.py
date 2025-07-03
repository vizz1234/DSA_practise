class Solution:
    def editDistance(self, s1, s2):
        # Base case: strings are already equal
        if s1 == s2:
            return 0

        n = len(s1)
        m = len(s2)

        # Initialize DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill base cases
        for i in range(n + 1):
            dp[i][0] = i  # Deleting all characters from s1

        for j in range(m + 1):
            dp[0][j] = j  # Inserting all characters of s2

        # Fill the table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # Characters match
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # Delete
                        dp[i][j - 1],    # Insert
                        dp[i - 1][j - 1] # Replace
                    )

        return dp[n][m]

sol = Solution()
print(sol.editDistance("horse", "ros"))