class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        lst=date.split(' ')
        dct={"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        day=''
        for i in lst[0]:
            if i.isnumeric():
                day+=i
        if len(day) == 1:
            day='0'+day
        return lst[2]+'-'+dct.get(lst[1])+'-'+day