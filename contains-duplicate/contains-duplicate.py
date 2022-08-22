from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value_map = defaultdict(int)
        
        for num in nums:
            value_map[num] += 1
        
        if any(value >= 2 for value in value_map.values()):
            return True
        else:
            return False