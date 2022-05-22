class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortArr=sorted(nums)
        d={}        
        for i in sortArr:
            d[i]=sortArr.index(i)
        new=[]
        for i in nums:
            new.append(d.get(i))
        return new