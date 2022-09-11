class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once=set(nums)
        print(once)
        sum=0
        for i in once:
            if nums.count(i) == 1:
                sum+=i
        return sum