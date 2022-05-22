class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        new=[]
        
        for i in range(len(candies)):
            test=[k for k in candies]
            test[i]+=extraCandies
            if test[i] == sorted(test)[-1]:
                new.append(True)
            else:
                new.append(False)
        return new        