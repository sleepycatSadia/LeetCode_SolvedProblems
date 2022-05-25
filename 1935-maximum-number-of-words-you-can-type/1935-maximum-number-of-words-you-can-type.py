class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
        text=text.split(' ')
        type=len(text)
        for i in text:
            for j in brokenLetters:
                if j in i:
                    type-=1
                    break
        return type