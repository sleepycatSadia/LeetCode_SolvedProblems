class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums :
            return 0
        else:
            s=''.join([str(i) for i in nums])
            if s.count('-') % 2 == 0 :
                return 1
            else:
                return -1