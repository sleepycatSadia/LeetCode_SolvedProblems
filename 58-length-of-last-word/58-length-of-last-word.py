class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        for i in s.split(' ')[::-1]:
            if i != '':
                return len(i)
