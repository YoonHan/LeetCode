class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin_str, y_bin_str = format(x, 'b').zfill(32), format(y, 'b').zfill(32)
        answer = 0
        for x_bit, y_bit in zip(x_bin_str, y_bin_str):
            if x_bit != y_bit:
                answer +=1
                
        return answer