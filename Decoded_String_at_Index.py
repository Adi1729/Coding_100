'''
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
'''

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        decode_s=""

        i=0
        index=0
        
        while(i<K):
            if S[index].isdigit():
                decode_s = decode_s * int(S[index])
            else:
                decode_s = decode_s + S[index]
            index = index + 1    
            i=len(decode_s)
           

        return (decode_s[K-1])
'''
# Solution from leetcode suggestions
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        length=0
        for char in S:
            if char.isdigit():
                length = length * int(char)
            else:
                length = length + 1
                
                
        for char in reversed(S):
            K = K % length
            if K==0 and char.isalpha():
                return char
            
            if char.isdigit():
                length = length/int(char)
            else: 
                length = length -1
                '''
       
