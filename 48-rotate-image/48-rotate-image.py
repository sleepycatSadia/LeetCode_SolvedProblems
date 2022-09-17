class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        for i in matrix[::-1]:
            for j in i:
                l.append(j)
                
        n=len(matrix)
        for i in range(n):
            idx=i
            for j in range(n):               
                matrix[i][j]=l[idx]
                idx+=n
        