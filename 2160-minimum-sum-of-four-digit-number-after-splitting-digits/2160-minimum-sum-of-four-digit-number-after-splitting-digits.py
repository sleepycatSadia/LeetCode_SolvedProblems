class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        l=sorted([int(i) for i in str(num)])
        
        return int(str(l[0])+str(l[2])) + int(str(l[1])+str(l[3]))