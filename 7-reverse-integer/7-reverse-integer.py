class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=''
        x=str(x)
        if str(x)[0]=='-':
            flag='-'
            x=x[1:]
        x=int(x[::-1])
        if x < -2**31 or x > (2**31 -1 ):
            return 0
        else:
            return int(flag+str(x))