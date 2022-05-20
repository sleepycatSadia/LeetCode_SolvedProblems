class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        #n=team count
        #m=match count
        m=0
        while(True):
            if n == 1:
                return m
            else:
                if n % 2 == 0:
                    m+=(n/2)
                    n=n/2
                else:
                    m+=((n-1)/2)
                    n=(n-1)/2 + 1

                #print('m ',m,' n ',n)