
'''
A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: N = 1, A = 2, B = 3
Output: 2
Example 2:

Input: N = 4, A = 2, B = 3
Output: 6
Example 3:

Input: N = 5, A = 2, B = 4
Output: 10
Example 4:

Input: N = 3, A = 6, B = 4
Output: 8

'''

# Solution 1 , Time limit exceeds
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """

        A_list=[i * A for i in range(1,N+1)]
        B_list=[i * B for i in range(1,N+1)]
        return sorted(list(set(A_list+B_list)))[N-1]
    

  # Solution 2 , percentile 20  
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """

        def hcf(a,b):
            while(b>0):
                a,b=b,a % b
            return a    

        def lcm(a,b):
            return(int(a*b/hcf(a,b)))



        lcm_ab=lcm(A,B)

        a_multiple = [i for i in range(A,lcm_ab+1,A)]
        b_multiple = [i for i in range(B,lcm_ab,B)]

        q=sorted(a_multiple+b_multiple)
        bucket_np= N//len(q)
        remainder = N % len(q)
        if remainder == 0:
            bucket_np = bucket_np-1
        
        w= [i+ lcm_ab * bucket_np for i in q][remainder-1]
        return w % (10**9 + 7)
