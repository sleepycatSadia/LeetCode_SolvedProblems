class Solution:
    def dayOfYear(self, date: str) -> int:
        def leapYear (year):
            return (year%4 == 0 and year%100 != 0) or (year%400 == 0) 
        
        
        d={0:0,1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334,12:365}
        part=date.split('-')
        if leapYear(int(part[0] )):
            d={0:0,1:31,2:60,3:91,4:121,5:152,6:182,7:213,8:244,9:274,10:305,11:335,12:366}
        return (d[int(part[1])-1])+int(part[2])