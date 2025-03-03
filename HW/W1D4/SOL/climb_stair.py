def climbStairs( n: int) -> int:
    if n < 3:
        return n
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]


    return dp[n]


print(climbStairs(2)) #2
print(climbStairs(3)) #3