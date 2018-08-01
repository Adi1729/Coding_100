# -*- coding: utf-8 -*-
'''
Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    
    def maxProfit(self, prices):
        
        """
        :type prices: List[int]
        :rtype: int
        """
        
        
        
        left_profit_list,right_profit_list=[],[]
        profit=0
        min_price,left_profit,max_price,right_profit=float('inf'),0,0,0
        

        for i in range(0,len(prices)):
            
            min_price=min(prices[i],min_price)
            left_profit=max(left_profit,prices[i]-min_price)
            left_profit_list.append(left_profit)
            
        for i in reversed(range(0,len(prices))):
            max_price=max(prices[i],max_price)
            right_profit=max(right_profit,max_price-prices[i])
            right_profit_list.insert(0,right_profit)
            
        for i in range(0,len(prices)):
            profit=max(profit,right_profit_list[i]+left_profit_list[i])
        
        return profit
