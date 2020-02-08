'''
source : https://www.hackerrank.com/contests/gs-codesprint/challenges/trader-profit/problem
logic: https://www.youtube.com/watch?v=oDhu5uGq_ic

https://python-forum.io/Thread-Creating-2D-array-without-Numpy
'''

a = [10,22,5,75,65,80]
a= np.array(a)
k = 2

dp = [0] * (k+1)
for i in range(k+1):
    dp[i] = [0] * len(a)

'''
rows : number of transaction
columns : days 
'''
i=1
j=2
for i in range(1,k+1):
    for j in range(1,len(a)):
        m=0
        while(m<j):
            dp[i][j]= max(dp[i][j-1],a[j] - a[m] + dp[i-1][m],dp[i][j])
            m=m+1