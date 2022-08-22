class Solution:
    def reverse(self, x: int) -> int:
        # check the argument number is in valid range
        def is_in_range(num):
            if (-2) ** 31 <= num and num <= 2 ** 31 - 1:
                return True
            else:
                return False
            
        if x > 0:
            reversed = int(str(x)[::-1])
        elif x == 0:
            return 0
        elif x < 0:
            reversed = -int(str(-x)[::-1])
            
        if is_in_range(reversed) == True:
            return reversed
        else:
            return 0
            