class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[str(i) for i in nums]
        return len(sorted((''.join(nums)).split('0'))[-1])
        