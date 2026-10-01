class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:

        pp = [0] * len(primes)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):

            np = [1] * len(primes)

            for idx, p in enumerate(primes):

                np[idx] = dp[pp[idx]] * p
            
            dp[i] = min(np)
            # print(np)
            # print(dp[i])

            for idx, p in enumerate(primes):

                if dp[i] == np[idx]:
                    pp[idx] += 1
            
        return dp[n - 1]

sol = Solution()
print(sol.nthSuperUglyNumber(12, [2, 3, 5]))