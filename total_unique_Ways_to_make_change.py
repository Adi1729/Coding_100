'''
source :https://www.youtube.com/watch?v=DJ4a7cmjZY0
https://www.hackerrank.com/challenges/coin-change/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
'''

amt = 5
coins =[0,1,2,5]
coins = [0] + coins.sort()
dp = [0] * len(coins)

for i in range(len(coins)):
    dp[i] =[0] * (amt+1)
    
for i in range(len(coins)):
    dp[i][0]=1

coins = [coin for coin in coins if coin <=amt]
    
for coin in range(1,len(coins)):
    for amt in range(amt+1):
        if coin > amt:
            dp[coin][amt] = dp[coin-1][amt]
        else:
            dp[coin][amt] = dp[coin][amt-coins[coin]] + dp[coin-1][amt]
dp[coin][amt]


amt = 18
coins =[49, 9 ,40, 17, 46, 24, 42, 26, 43, 41, 35 ,1, 47, 28, 20, 38, 2, 44, 32, 22, 18, 45, 25]