class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum=0
        for i in range(len(arr) + 1):
            for j in range(i):
                if len(arr[j:i]) % 2 == 1:
                    for k in arr[j:i]:
                        sum+=k
        return sum