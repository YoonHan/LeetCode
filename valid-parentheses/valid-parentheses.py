class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        
        stack = []
        for parenthesis in s:
            if len(stack) == 0:
                stack.append(parenthesis)
            elif stack[-1] == '(' and parenthesis == ')':
                stack.pop()
            elif stack[-1] == '{' and parenthesis == '}':
                stack.pop()
            elif stack[-1] == '[' and parenthesis == ']':
                stack.pop()
            else:
                stack.append(parenthesis)
        
        return len(stack) == 0