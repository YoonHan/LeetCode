from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        characterMap = defaultdict(int)
        for letter in ransomNote:
            characterMap[letter] += 1
            
        for letter in magazine:
            characterMap[letter] -= 1
            
        return all(remainingCount <= 0 for remainingCount in characterMap.values())
