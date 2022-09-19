class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        c=0
        for i in range(len(s)-k+1):
            print(int(s[i:i+k]))
            if int(s[i:i+k]) != 0 and num % int(s[i:i+k]) == 0:
                c+=1
        # if len(s) == 1 and num % k == 0:
        #     c+=1
        return c