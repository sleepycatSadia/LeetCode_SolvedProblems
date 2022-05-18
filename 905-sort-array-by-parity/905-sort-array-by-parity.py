class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        odd=[]
        for i in nums:
            if i%2==0:
                l.append(i)
            else:
                odd.append(i)
        return l+odd
        