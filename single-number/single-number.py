class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use XOR bitwise operation
        # if a number XORed twice, the number has no effect on the result
        answer = 0
        for num in nums:
            answer ^= num
        return answer