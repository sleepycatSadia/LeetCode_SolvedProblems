class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=[]
        sortedHeight=sorted(heights,reverse=True)
        for i in sortedHeight:
            l.append(names[heights.index(i)])
            #print(l)
        return l