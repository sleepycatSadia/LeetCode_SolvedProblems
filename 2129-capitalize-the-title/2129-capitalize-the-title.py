class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        return ''.join(i[0].upper()+i[1:].lower()+' ' if len(i)>2 else i.lower()+' '  for i in title.split(' ') )[:-1:]
        