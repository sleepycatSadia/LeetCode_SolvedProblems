class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        n=list(map(int, str(n)))
        p=1
        for i in n:
            
            p*=int(i)
        return p-sum(n) 