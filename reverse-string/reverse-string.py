class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first_index, last_index = 0, len(s) - 1
        
        while first_index < last_index:
            s[first_index], s[last_index] = s[last_index], s[first_index]
            first_index += 1
            last_index -= 1