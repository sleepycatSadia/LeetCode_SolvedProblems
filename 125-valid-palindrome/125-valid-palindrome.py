class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s2=''
        for i in s:
                if i.isalnum():
                    s2+=i
        if s2 == s2[-1:-(len(s2))-1:-1] :
            return True
        return False
        