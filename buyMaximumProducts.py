'''
source :
https://www.hackerrank.com/contests/gs-codesprint/challenges/buy-maximum-stocks
'''

n = 5
arr =[49, 100, 100,100, 10]
k =50

i=0
stocks_total=0


for i in range(1,n+1):    
    s=  (i) * a[i-1]
    stocks_total = stocks_total + (i)
    k = k - s
    if k==0:
        print(stocks_total)
        break
    elif k<0:
        k = k +s
        stocks_total  = stocks_total -i
        break

for j in range(1,i+1):
    k = k - a[i-1]
    if k==0 :
        print(stocks_total +1)
        break
    elif (k<0):
        print(stocks_total)
        break
    else:
        stocks_total = stocks_total+1



import sys

def buyMaximumProducts(n, k, a):
    i=0
    stocks_total=0
    import operator
    days = [i for i in range(1,len(a)+1)]
    dict_a = list(tuple(zip(a,days)))
    
    dict_a.sort(key = operator.itemgetter(0))
    
    for price,number_of_stock in dict_a:
        print(price, number_of_stock)
        s=   price * number_of_stock
        stocks_total = stocks_total + number_of_stock
        k = k - s
        if k==0:
            return stocks_total
        elif k<0:
            k = k +s
            stocks_total  = stocks_total -  number_of_stock 
            break
        
    for j in range(1, number_of_stock):
        k = k - a[i-1]
        if k==0 :
            return stocks_total +1
        elif (k<0):
            return stocks_total
        else:
            stocks_total = stocks_total+1
            

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)
    
    
from itertools import product   
# Get all permutations of length 2 
# and length 2 
perm = permutations([1, 2, 3,4], 4)
N=4
res = [ele for ele in product(range(1, N + 1), repeat = 3)] 
import numpy as np
q=np.array(res[0])
w= [1,2,3]
for i in perm:
    print(i)