class Solution:
    def fib(self, n: int) -> int:
        n0=0
        n1=1
        if n == 0:
            return n0
        elif n == 1:
            return n1
        else:
            while n >= 2 :
                sum=n0+n1
                n0=n1
                n1=sum
                n-=1
            return sum