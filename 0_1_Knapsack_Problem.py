'''
source : 'https://www.youtube.com/watch?v=8LusJS5-AGo'
'''
import numpy as np

#input1
items = {0:0,
        1:6,
         2:10,
         3:12}

maxWeight = 5

#input2
items = {0:0,
        1:1,
         3:4,
         4:5,
         5:7}


maxWeight = 7
weights = list(items.keys())

dp=[[0]*(maxWeight+1)]*(5)

dp = np.array(dp)

for j in range(5):
    dp[j][0] = 0
       
for i in range(1,5):
    for j in range(1,maxWeight+1):
        if j-weights[i]>=0:
            dp[i][j] = max(dp[i-1][j] , items[weights[i]] + dp[i-1][j-weights[i]])
        else:
            dp[i][j] = max(dp[i][j] , dp[i-1][j])