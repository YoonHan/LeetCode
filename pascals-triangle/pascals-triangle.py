class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        
        answer = []
        for rowNum in range(1, numRows + 1):
            row = []
            for index in range(rowNum):
                if index == 0:
                    row.append(1)
                elif index == rowNum - 1:
                    row.append(1)
                else:
                    row.append(answer[rowNum - 1 - 1][index - 1] + answer[rowNum - 1 - 1][index])
            answer.append(row)
        
        return answer