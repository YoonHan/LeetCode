class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_binary_integer = int(format(n, 'b').zfill(32)[::-1], 2)
        return reversed_binary_integer