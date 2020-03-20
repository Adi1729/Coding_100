'''
source : https://www.hackerrank.com/challenges/sherlock-and-cost/problem
'''

'''
logic : https://www.hackerrank.com/challenges/sherlock-and-cost/editorial
'''

b =[4,7,9]
k = len(b)

dp = [0] * (k)
for i in range(k):
    dp[i] = [0] * 2

i=1
for i in range(1, k):
    for j_0 in [1, b[i-1]]:
        for j_1 in [1, b[i]]:
            col = 0 if j_0 ==1 else 1 
            if j_1 ==1:
                dp[i][0]  = max(dp[i][0], abs(j_1-j_0) + dp[i-1][col])
            else:
                dp[i][1]  = max(dp[i][1], abs(j_1-j_0) + dp[i-1][col])


print(max(dp[k-1][0],dp[k-1][1]))

