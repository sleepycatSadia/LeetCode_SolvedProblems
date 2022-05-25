class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return ''.join([item+' ' for item in  s.split(' ')[0:k] ] )[:-1:]
        
        