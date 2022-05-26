class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lst=[]
        words=sorted(words,key=len)
        x=words[0]
        for ch in x:
            flag=True
            for idx in range(1,len(words)):
                if ch not in words[idx] or (words[idx].count(ch) < lst.count(ch) + 1 ):
                    flag=False
                    break
            if flag :
                lst.append(ch)
        return lst