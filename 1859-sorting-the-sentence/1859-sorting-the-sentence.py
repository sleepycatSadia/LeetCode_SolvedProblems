class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        d={}
        for i in s :
          d[i[-1]]=i[0:-1:]
        l=sorted(d)
        s=''
        for i in range(len(l)) :
          s+=d[l[i]]
          if not i == len(l)-1 :
            s+=' '
        
        return s