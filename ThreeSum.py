'''
Given a list of integers, write a function that returns all sets of 3 numbers in
the list, a, b, and c, so that a + b + c == 0.

threeSum({​ -1​ , ​ 0 ​ , ​ 1 ​ , ​ 2 ​ , ​ -1​ , ​ -4​ })
[​ -1​ , ​ -1​ , ​ 2 ​ ]
[​ -1​ , ​ 0 ​ , ​ 1 ​ ]

'''

#BruteForce
a= [-1,0,-2,1,4,-4]
a=np.array(a)
sumzero=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            s= a[i] + a[j] + a[k]
            if s==0:
                sumzero.append((a[i],a[j],a[k]))
                


