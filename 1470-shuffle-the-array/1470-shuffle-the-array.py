class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new=[]
        for i in range(n):
            new.append(nums[i])
            new.append(nums[n+i])
        return new