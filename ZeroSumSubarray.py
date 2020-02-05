import numpy as np
a=[1,2,-5,1,2,-1]
a=np.array(a)


# o(n**2)
for i in range(len(a)):
    for j in range(i,len(a)):n
        s= s+ a[j]
        if s == 0:
            print(s,i,j)
         

'''
source : https://www.youtube.com/watch?v=Ofl4KgFhLsM
'''

a= [1,4,20,3,10,5]
a=np.array(a)
s=0
subarray = 33
left=0
i=4
a[4]
for i in range(len(a)):
    right = i
    s = s+a[i]
    while s>subarray:
        s=s-a[left]
        left+=1
    if s== subarray:
        break
    

'''
source: https://www.youtube.com/watch?v=AvyGBuji7ro
'''

'''
running sum has to be zero or it has to occur twice
'''
a =[1,2,-5,1,2,-5,1,1]
a=np.array(a)

s=0
running_sum={}
max_len=0
for i in range(len(a)):
    s= s + a[i]
    if s not in running_sum:
        running_sum[s]=i
    if s in running_sum:
        max_len = max(max_len,i - running_sum[s])
    if s==0:
        max_len = max(max_len,i)
    
    sum.append(s)
    
    
    
            
    