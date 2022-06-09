class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        l=[]
        for i in ransomNote:
            if i not in l:
                if ransomNote.count(i) > magazine.count(i) :
                    return False
                l.append(i)
        return True