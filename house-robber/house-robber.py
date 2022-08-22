class Solution:
    def rob(self, nums: List[int]) -> int:
        memorised = {}
        def find_maximum_money(index):
            # recursion end condition
            if index > len(nums) - 1:
                return 0
            # get candidate 1 of maximum value  
            if index + 2 in memorised: 
                candidate1 = nums[index] + memorised[index + 2]
            else:
                candidate1 = nums[index] + find_maximum_money(index + 2)
            # get candidate 2 of maximum value
            if index + 1 in memorised:
                candidate2 = memorised[index + 1]
            else:
                candidate2 = find_maximum_money(index + 1)
            memorised[index] = max(candidate1, candidate2)
            return memorised[index]
            
        return find_maximum_money(0)
