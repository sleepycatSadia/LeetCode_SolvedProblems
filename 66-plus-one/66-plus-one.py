class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def func(idx,inc,digits):
            if idx == -len(digits)-1 and inc == 1:
                digits[0]=1
                digits.append(0)
                return 
                
            else:
                if digits[idx]+inc ==10:
                    digits[idx]=0
                    func(idx-1,1,digits)                       
                else: 
                    digits[idx]=digits[idx]+1
            return digits

        return func(-1,1,digits)
