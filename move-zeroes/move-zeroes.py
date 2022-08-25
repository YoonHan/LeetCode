class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total_length = len(nums)
        
        # find the first index of zero
        first = None
        for i in range(total_length):
            if nums[i] == 0: 
                first = i
                break
        
        # modify nums in-place
        if first != None:
            for i in range(first + 1, total_length):
                if nums[i] == 0:
                    continue
                else:
                    nums[first], nums[i] = nums[i], nums[first]
                    first += 1
                    
        
        