class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        while(True):
            if num == 0 :
                return c
            else:
                c+=1
                if num % 2 == 0 :
                    num/=2
                else:
                    num-=1