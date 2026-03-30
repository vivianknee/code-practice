class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #always starts with 1
        res = [[1]]
        
        #iteration for total num of rows
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            #building the next row which is prev row + 1
            for j in range(len(res[-1]) + 1):
                row.append(temp[j]+ temp[j+1])
            res.append(row)
        return res
            
        


        