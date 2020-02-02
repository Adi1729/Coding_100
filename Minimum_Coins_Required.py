# Python 3 program to find minimum 
# number of denominations 
#
#def findMin(V): 
#	
#	# All denominations of Indian Currency 
#	deno = [2,5,8]
#	n = len(deno) 
#	
#	# Initialize Result 
#	ans = [] 
#
#	# Traverse through all denomination 
#	i = n - 1
#	while(i >= 0): 
#		
#		# Find denominations 
#		while (V >= deno[i]): 
#			V -= deno[i] 
#			ans.append(deno[i]) 
#
#		i -= 1
#
#	# Print result 
#	for i in range(len(ans)): 
#		print(ans[i], end = " ") 
#
## Driver Code 
#if __name__ == '__main__': 
#	n = 11
#	print("Following is minimal number", 
#		"of change for", n, ": ", end = "") 
#	findMin(n)
	
# This code is contributed by 
# Surendra_Gangwar 


# This code is contributed by Afzal Ansari 
sum=11
dp = [[sum+1]*(sum+1)]*5
dp = np.array(dp)
coins =[1,2,5,8]
for coin in range(5):
    dp[coin][0] = 0
for i in range(1,5):
    for j in range(1,sum+1):
        dp[i][j] = min(dp[i][j-coins[i-1]] +1 , dp[i-1][j])
        