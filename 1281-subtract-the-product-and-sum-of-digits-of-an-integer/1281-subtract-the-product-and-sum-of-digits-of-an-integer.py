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
'''
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s,p=0,1
        for i in list(str(n)):
            s+=int(i)
            p*=int(i)
        return p-s    
 class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=[int(i) for i in (str(n))]
        p=1
        for i in n:
            
            p*=int(i)
        return p-sum(n)
'''