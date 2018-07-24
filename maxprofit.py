# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:27:19 2018

@author: aditya
"""
'''
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
             
             '''
prices=  [7,1,5,3,6,4]
prices= [7,6,4,3,1]
diff=[]

min_price = float('inf')
max_profit =0
for i in range(0,len(prices)):
    
    if(prices[i]< min_price):
        min_price= prices[i]
    elif (prices[i]-min_price > max_profit):
        max_profit = prices[i]-min_price
  
            
            
print(max(diff))
            
    