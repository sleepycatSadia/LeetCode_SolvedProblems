class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[-1:-(len(str(x)))-1:-1] :
            return True
        return False
        