class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        r=[]
        for i in queries:
            c=0
            for j in points:
                if ((j[0]-i[0])**2 + (j[1]-i[1])**2) <= i[2]**2 :
                    c+=1
                    #print (j)
            r.append(c)
        return r