class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split(' ')
        d={}
        if len(pattern) != len (s) :
            return False
        else:
            for i in range(len(s)):
                if pattern[i] in d :
                    if d.get(pattern[i]) != s[i]:
                        return False
                else:
                    if s[i] in d.values():
                        return False
                    else:
                        d[pattern[i]]=s[i]
                        
            return True