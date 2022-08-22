class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        stack = [s[0]]
        
        # convert a roman combination into number
        for roman in s[1:]:
            last_element = stack[-1]
            if last_element == 'I' and (roman == 'V' or roman == 'X'):
                stack.pop()
                stack.append(roman_num_map[roman] - roman_num_map[last_element])
            elif last_element == 'X' and (roman == 'L' or roman == 'C'):
                stack.pop()
                stack.append(roman_num_map[roman] - roman_num_map[last_element])
            elif last_element == 'C' and (roman == 'D' or roman == 'M'):
                stack.pop()
                stack.append(roman_num_map[roman] - roman_num_map[last_element])
            else:
                stack.append(roman)
        
        # get total sum of roman letter
        return sum(map(lambda element: roman_num_map[element] if type(element) != int else element, stack))
            
            
            