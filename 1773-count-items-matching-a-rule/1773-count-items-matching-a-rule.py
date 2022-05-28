class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        if ruleKey == 'color' :
            key = 1
        elif ruleKey == 'name' :
            key = 2
        else:
            key=0
        count=0
        
        for i in items:
            if i[key]==ruleValue:
                count+=1
        return count
        