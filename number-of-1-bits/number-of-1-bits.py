class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = format(n, 'b')
        return binary_string.count('1')