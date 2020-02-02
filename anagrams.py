s= 'cbaebabacd'
a = 'abc'
s="ababababab"
a="aab"


a ='acb'
q= [i for i in a]
q.sort()
a = ''.join(q)

a_orig =a
b= 'b'
l=[]
i=0
i=1
pcounter = collections.Counter(a)
scounter = collections.Counter(s[:len(a)])
for i in range(0,len(s)-len(a)+1):
    scounter = collections.Counter(s[i:len(a)+i])
    if pcounter==scounter:
        l.append(i)
        
c='a'
a_orig ='abc'
a=a_orig

p=a

 #Method 1 : Using Counters
        result = []
        pcounter = collections.Counter(p)
        scounter = collections.Counter(s[:len(p) - 1])
        begin = 0
        for i in range(len(p) - 1, len(s)) : 
            scounter[s[i]] += 1
            if scounter == pcounter : 
                print(scounter)
                result.append(begin)
            
            scounter[s[begin]] -= 1
            if scounter[s[begin]] == 0 : 
                del(scounter[s[begin]])
            
            begin += 1
        
        return result

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

a='ate'
l = [i for i in a]
l.sort()

q = ''.join(l)







