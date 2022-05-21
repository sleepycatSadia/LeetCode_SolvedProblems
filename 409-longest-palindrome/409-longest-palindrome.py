class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for  i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1              
        length=0
        odd={}
        for i in d:
            if d[i]%2 == 0:
                length+=d[i]
            else:
                odd[i]=d[i]      
        if len(odd)>=1:    
            lst=sorted(odd.values(),reverse=True)
            for i  in range(1,len(lst)):
                length+=(lst[i]-1)
            return length+lst[0]
        else:
            return length