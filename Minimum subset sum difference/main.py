def minimumDifference(nums) -> int:

    total = sum(nums)
    n = len(nums)

    def subsetSum():
        dp = [[False for i in range(total+1)] for j in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, total+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        possible = []
        for j in range(total//2, -1, -1):
            if dp[n][j] == True:
                possible.append(j)
        return possible

    ans = total
    lst = subsetSum()
    for i in range(len(lst)):
        ans = min(ans, total - 2*lst[i])
    return ans

nums = list(map(int, input().strip().split()))
print(minimumDifference(nums))
