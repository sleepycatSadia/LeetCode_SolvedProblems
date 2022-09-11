class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=[0]
        idx=0
       
        for i in gain:
            rn=alt[idx]
            alt.append(rn+i)
            idx+=1
        return sorted(alt)[-1]