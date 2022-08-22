class Solution:
    def isPalindrome(self, s: str) -> bool:   
        alphanumerics = []
        for letter in s:
            if letter.isalnum():
                alphanumerics.append(letter.lower())
        
        if len(alphanumerics) == 0: 
            return True
        else:
            for original_letter, reversed_letter in zip(alphanumerics, reversed(alphanumerics)):
                if original_letter != reversed_letter:
                    return False
            return True
                