class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink=numBottles
        while(numBottles >= numExchange):
            drink+=numBottles//numExchange
            numBottles=int(numBottles%numExchange)+numBottles//numExchange
        return drink