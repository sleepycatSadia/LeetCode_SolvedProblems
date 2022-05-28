class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=''
        l=[]
        for i in s:
            if i == 'a' or i =='e' or i =='i' or i == 'o' or i== 'u' or i == 'A' or i =='E' or i =='I' or i == 'O' or i== 'U':
                l.append(i)
                
        for i in s:
            if not (i == 'a' or i =='e' or i =='i' or i == 'o' or i== 'u' or i == 'A' or i =='E' or i =='I' or i == 'O' or i== 'U'):
                n+=i
            else:
                n+=l.pop(-1)
        return n