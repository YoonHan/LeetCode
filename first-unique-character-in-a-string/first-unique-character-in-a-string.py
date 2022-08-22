from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_count_map = defaultdict(int)
        for letter in s:
            letter_count_map[letter] += 1
        
        # find first non-repeating character's index
        for letter, count in letter_count_map.items():
            if count == 1:
                return s.find(letter)
        return -1