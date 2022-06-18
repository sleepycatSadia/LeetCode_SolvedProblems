class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range (1,1+n):
            print(str(bin(i)))
            if str(bin(i))[2::] not in s :
                return False
        return True