class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        sum=0
        for i in nums:
            sum+=i
            l.append(sum)
            
        return l