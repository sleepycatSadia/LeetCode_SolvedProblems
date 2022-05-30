class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        idx=0
        
        for lst in mat :
            sum+=lst[idx]+lst[len(mat)-idx-1]
            idx+=1
        
        if len(mat) % 2 == 0:
            return sum
        return sum - mat[len(mat)//2][len(mat)//2]