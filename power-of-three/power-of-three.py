import math
import sys

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # finding maximum (3 ^ n) format number less than (2 ^ 31 - 1)
        #
        # n = 1
        # while n * 3 <= 2 ** 31 - 1:
        #    n *= 3
        # print(n) 
        # >> 1162261467
        return n > 0 and 1162261467 % n == 0
        
        
        