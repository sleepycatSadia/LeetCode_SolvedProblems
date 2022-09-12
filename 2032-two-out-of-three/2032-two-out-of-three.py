class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))
        numList=nums1+nums2+nums3
        numSet=set(numList)
        distinct=[]
        for i in numSet:
            if numList.count(i)>=2:
                distinct.append(i)
        return distinct
        
        