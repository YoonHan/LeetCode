class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_map = list(map(lambda x: str(x), digits))
        num = int(''.join(str_map))
        return list(str(num + 1))
        
        