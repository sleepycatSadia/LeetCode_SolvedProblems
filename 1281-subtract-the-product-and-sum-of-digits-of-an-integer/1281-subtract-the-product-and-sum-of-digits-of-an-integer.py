class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy

        n=list(map(int, str(n)))
        return numpy.prod(n)-sum(n)    