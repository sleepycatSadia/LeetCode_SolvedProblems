class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            equal=True
            for i in s:
                if s.count(i) != t.count(i):
                    equal=False
                    break
            if not equal:
                return False
            else:
                return True