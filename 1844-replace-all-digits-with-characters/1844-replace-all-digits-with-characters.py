class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        for i in range(1,len(s),2):
            s[i]=chr(ord(s[i-1])+int(s[i]))
        return ''.join([c for c in s])
            