class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        if len(s) != len (t) :
            return False
        else:
            for i in range(len(s)):
                if s[i] in d :
                    if d.get(s[i]) != t[i]:
                        return False
                else:
                    if t[i] in d.values():
                        return False
                    else:
                        d[s[i]]=t[i]
                        
            return True