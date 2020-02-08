'''

Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it is able to trap after raining.

https://www.geeksforgeeks.org/trapping-rain-water/
'''

import numpy as np

a = [2,0,2]
a=np.array(a)

for i in range(1,len(a)-1):
    if a[i] < a[i-1] :
        s=0
    if