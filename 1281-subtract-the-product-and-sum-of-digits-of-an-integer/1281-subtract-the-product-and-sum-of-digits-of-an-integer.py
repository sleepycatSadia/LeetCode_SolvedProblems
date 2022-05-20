class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=list(map(int, str(n)))
        p=1
        for i in n:
            
            p*=int(i)
        return p-sum(n)    
