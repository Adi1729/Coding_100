'''
https://www.hackerrank.com/challenges/construct-the-array/problem

There are two cases :

1. when array has sequence 1..not 1
2. when array has sequence 1 ..1

'''

def countArray(n, k, x):
    m = 1000000007
    dp = [0] * n
    for i in range(n):
        dp[i] = [0] * 2

    if (x != 1):
        dp[0][0] = 1
        dp[0][1] = 0
        dp[1][0] = k - 2
        dp[1][1] = 1

    else:
        dp[0][0] = 0
        dp[0][1] = 1
        dp[1][0] = k - 1  # if x==1, there are k-1 options
        dp[1][1] = 0  # array can not be 1-1

    for i in range(2, n):
        dp[i][0] = (dp[i - 1][0] * (k - 2) + dp[i - 1][1] * (k - 1)) % m
        dp[i][1] = (dp[i - 1][0]) % m

    return dp[n - 1][1] % m