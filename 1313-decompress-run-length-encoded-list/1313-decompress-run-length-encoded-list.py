class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in range(0,len(nums),2):
            for k in range(nums[i]):
                new.append(nums[i+1])
        return new