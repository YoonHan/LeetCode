class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        result = [nums[0]]
        for index, num in enumerate(nums[1:]):
            result.append(result[index] + num)
            
        return result