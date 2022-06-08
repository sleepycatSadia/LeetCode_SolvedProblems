class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        if  ( coordinates [0] in 'bdfh' and  int(coordinates [1]) % 2 == 1 ) or  (coordinates [0] in 'aceg' and  int(coordinates [1]) % 2 == 0 ):
            return True
        return False