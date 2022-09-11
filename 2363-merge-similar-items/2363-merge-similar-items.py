class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        item=items1+items2
        #print(sorted(item))
        item.sort()
        ret=[]
        idx=0

        while(True):
            val=item[idx][0]

            sum=0
            while(True):


                if  idx == len(item) or val != item[idx][0] :
                        ret.append([val,sum])
                        #print(ret)
                        break
                else:
                    #print("val=",val,'idx=',idx,'item[idx][0]',item[idx][0])
                    if val == item[idx][0]:
                        sum+=item[idx][1]

                        idx+=1
                        #print('sum=',sum,'idx=',idx)


            if idx == len(item):
                break
        return ret