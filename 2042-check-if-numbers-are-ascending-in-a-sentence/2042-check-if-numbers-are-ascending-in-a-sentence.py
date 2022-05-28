class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s.split(' '):
            if i.isnumeric():
                l.append(int(i))
        
        s=sorted(l)
        for i in range(len(s)):
            if s[i] != l [i] or s.count(s[i])>1:
                return False
        return True
            