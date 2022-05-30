class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s= s+t
        for i in s:
            if s.count(i) % 2 == 1:
                return i