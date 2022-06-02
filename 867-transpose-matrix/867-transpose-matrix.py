class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy as np
        gfg=np.array(matrix)
        return gfg.transpose()