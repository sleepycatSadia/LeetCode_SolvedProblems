class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        l=[]
        for i in accounts:
            sum=0
            for j in i:
                sum+=j
            l.append(sum) 
            
        l.sort()
        return l[-1]
        