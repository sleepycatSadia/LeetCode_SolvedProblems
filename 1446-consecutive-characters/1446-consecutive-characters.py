class Solution:
    def maxPower(self, s: str) -> int:
        max=0
        ch=s[0]
        val=0
        for i in s[0:]:
            #print(f'i={i} ch= {ch}')
            if i == ch :
                val+=1
                if val > max :
                    max=val
                    #print(f'max {max} for ch {ch} ')
            else:
                
                val=1
                ch=i
        return max