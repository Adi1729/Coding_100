'''
Regex matching problem¶

    "?" matches a single character

    "*" matches zero or more charcters

    Given a pattern(p) and a string(s), does p match s?

    examples:
        TRUE: ("*", "ab"), ("?a" ,"ba"), ("?a" ,"aa"), ("a*" ,"a")
        FALSE: ("*a", "ab"), ("?a" ,"baa"), ("?a" ,"a"), ("a*" ,"ba")

    Very popular interview question at product-based companies for SDEs.

    Small variations of this are often used in interviews


Method 1 : Using Recursion
Method 2 : Using Dynamic Programming with recursion (Top- down approach)
Method 3 : Using Dynamic Programming with iteration (Bottom - up approach)
'''


# Method 1

def isMatch(p,s):

    print(p,s)

    if p==s:
        return True

    if p=='*':
        return True

    if p=='' or s=='':
        return False

    if p[0]==s[0] or p[0]=='?':
        return isMatch(p[1:],s[1:])

    if p[0] == '*':
        return (isMatch(p,s[1:]) or isMatch(p[1:], s))

    if p[0]!=s[0]:
        return False

#print(isMatch('*a','caa'))

# Method 2 : Dynamic Programming with recursion

def isMatch_DP_with_recursion(pattern,string,p_start, s_start,dp):

    '''
    --------------------
    Parameters :
    --------------------

     pattern: pattern
     string: string
     p_start: starting index of pattern p
     s_start: starting index of pattern s
     dp: dictionary storing results of dynamic programming

    '''

    p = pattern[p_start:]
    s = string[s_start:]
    tmp  = True
    print(p,s,p_start,s_start,dp)

    if p==s:
        dp[(p_start,s_start)]=True
        p_start = p_start+1
        s_start = s_start+1
        return True

    elif p=='*':
        dp[(p_start,s_start)]=True
        p_start = p_start + 1
        s_start = s_start + 1
        return True

    elif p=='' or s=='':
        dp[(p_start,s_start)]=False
        p_start = p_start + 1
        s_start = s_start + 1
        return False

    elif p[0]==s[0] or p[0]=='?':
        p_start = p_start + 1
        s_start = s_start + 1
        tmp = isMatch_DP_with_recursion(p,s,p_start,s_start,dp)
        dp[(p_start,s_start)] = tmp
        return tmp

    elif p[0] == '*':
        tmp = isMatch_DP_with_recursion(p,s,p_start,s_start + 1,dp) or isMatch_DP_with_recursion(p,s,p_start+1,s_start,dp)
        dp[(p_start, s_start)] = tmp
        return tmp

    elif p[0]!=s[0]:
        dp[(p_start,s_start)]=False
        return False

#print(isMatch_DP_with_recursion('*a','caa',0,0,{}))
#print(isMatch_DP_with_recursion('?a','caa',0,0,{}))
#print(isMatch_DP_with_recursion('*a','caa',0,0,{}))
#print(isMatch_DP_with_recursion('*a','caa',0,0,{}))


# Method 3 : Dynamic Programming with iteration/tabulation
        
def isMatch_DP_with_tabulation(p,s):
    
    '''
    -------------
    parameters:
    -------------
    
    p : pattern
    s : string
    
    source : https://www.youtube.com/watch?v=3ZDZ-N0EPV0
    
    '''
        
    
    n = len(s) # string length
    m = len(p) # pattern length
    
    dp = [0] * (n+1)
    
    for i in range(n+1):
        dp[i] = [0] * (m+1)
    
    '''
      ------------------
       pattern  - columns
       string  - rows
    '''
    
    # filling 0th row of pattern:
    dp[0][0] = True
    
    for i in range(1,m+1):
        dp[0][i] = p[i-1]=='*'
        
  #
  #      or initialize using below logic 
  #  for i in range(1,m+1):
   #       if p[i-1] == '*' :
                  #dp[0][i] = dp[0][i-1]

        
        
    # filling 0th columns of string:
    for i in range(1,n+1): 
        dp[i][0] = False
        
    for i in range (1,n+1):
        for j in range(1,m+1):
            if p[j-1] == s[i-1] or p[j-1]=='?' :
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] != s[i-1]:
                dp[i][j] = False
                
    return dp[i][j]
    

p = '*a'
s = 'caa'     
print(isMatch_DP_with_tabulation('*a','caa'))
print(isMatch_DP_with_tabulation('?aa','caa'))
print(isMatch_DP_with_tabulation('*a','caa'))
print(isMatch_DP_with_tabulation('*a','cba'))
print(isMatch_DP_with_tabulation('*?a','cba'))
    
    
