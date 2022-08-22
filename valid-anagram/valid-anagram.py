from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_map1 = defaultdict(int)
        letter_map2 = defaultdict(int)
        
        # make count-by-letter map
        for letter in s:
            letter_map1[letter] += 1
            
        for letter in t:
            letter_map2[letter] += 1
        
        
        # check two maps are equal
        keys1 = letter_map1.keys()
        keys2 = letter_map2.keys()
        if len(keys1) != len(keys2): 
            return False
        
        for key in keys1:
            if key not in keys2 or letter_map1[key] != letter_map2[key]:
                return False
        return True
        