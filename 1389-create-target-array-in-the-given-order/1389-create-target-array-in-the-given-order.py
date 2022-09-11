class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target=['bleh']*len(nums)
        count=0
        for i in index:
            if target[i] == 'bleh':
                target[i]=nums[count]
            else:
                target=target[0:i]+[nums[count]]+target[i:-1]
            count+=1
            #print(target)
        return target
