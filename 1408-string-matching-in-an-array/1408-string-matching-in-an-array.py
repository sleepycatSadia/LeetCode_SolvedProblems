class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        #print(words)
        ret=[]
        for i in words:
            words=words[1:]
            #print(words)
            for w in words[::-1]:
                #print('i=',i,' w=',w)
                if i in w and i not in ret:
                    ret.append(i)
            #print('ret',ret)
        return ret