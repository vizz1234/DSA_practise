def is_subset_sum(arr, total_sum):
    n = len(arr)
    dp = [[False] * (total_sum + 1) for _ in range(n + 1)]

    # If sum is 0, then answer is True (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the subset table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]  # can't include arr[i-1]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][total_sum]

arr = [3, 34, 4, 12, 5, 2]
total_sum = 9
print(is_subset_sum(arr, total_sum))
