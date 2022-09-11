class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=[i for i in s]
        alpha=[]
        for char in s:
            if char.isalpha() :
                alpha.append(char)
        #print(alpha)
        alpha.reverse()
        #print(alpha)
        idx=0
        for i in range(len(s)):
            if s[i].isalpha():
                s[i]=alpha[idx]
                idx+=1
        return ''.join(i for i in s)