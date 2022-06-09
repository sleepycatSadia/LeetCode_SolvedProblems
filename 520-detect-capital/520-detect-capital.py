class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        upper=0
        for i in word:
            if i.isupper():
                upper+=1
        if upper == len(word) or upper == 0 or (word[0].isupper() and upper == 1):
            return True
        return False