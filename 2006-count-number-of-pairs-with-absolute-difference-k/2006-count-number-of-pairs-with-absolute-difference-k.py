class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        import math
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] - nums[j] < 0 :
                    if -nums[i] - nums[j] == k:
                        c+=1
                else:
                    if nums[i] - nums[j] == k:
                        c+=1
                                  
        return c  