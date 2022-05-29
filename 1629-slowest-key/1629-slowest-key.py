class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        d={keysPressed[0]:releaseTimes[0]}
        for i in range(1,len(keysPressed)):
            if  releaseTimes[i] - releaseTimes[i - 1]  >= max (d.values()):
                if keysPressed[i] in d:
                    d[keysPressed[i]]=max(d.get(keysPressed[i]),(releaseTimes[i] - releaseTimes[i - 1]))
                    #print(releaseTimes[i] - releaseTimes[i - 1])
                else:
                    d[keysPressed[i]]=releaseTimes[i] - releaseTimes[i - 1]
        slow=max(d.values())
        #print(d)
        l=[]
        for i,j in d.items():
            if j == slow :
                l.append(i)
        return sorted(l)[-1] 