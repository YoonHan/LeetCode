class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        initial_list_length = len(nums)
        pivot_value = nums[0]
        next_replace_index = 1
        
        if initial_list_length == 1: 
            return 1
        
        # mark duplicate numbers as '_'
        for index in range(1, initial_list_length):
            if pivot_value != nums[index]:
                nums[next_replace_index] = nums[index]
                next_replace_index += 1
                pivot_value = nums[index]
        
        return next_replace_index