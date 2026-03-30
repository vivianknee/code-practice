class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return matrix values in spiral order
        # l and r traverse cols
        # bottom and top traverse rows
        res = []
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        # once l exceeds r, we've gotten to the center of the matrix
        while l <= r and top <= bottom:
            # iterate for the length of the matrix
            for i in range(l, r + 1): # stop before the last to avoid double appending
                # for top left to top right
                res.append(matrix[top][i]) 
            top += 1

            for i in range(top, bottom + 1): 
                # for top right to bottom right
                res.append(matrix[i][r])  
            r -= 1
            if top <= bottom:
                for i in range(r, l - 1, -1): 
                    # for bottom right to bottom left
                    res.append(matrix[bottom][i])
                bottom -= 1
                
            if l <= r:
                for i in range(bottom, top - 1, -1): 
                    # for bottom left to top left
                    res.append(matrix[i][l])
                l += 1
        
        return res
            


