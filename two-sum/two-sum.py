class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memorised_map = {}
        for index, num in enumerate(nums):
            if num in memorised_map:
                return [nums.index(memorised_map[num], 0, index), index]
            else:
                memorised_map[target - num] = num
