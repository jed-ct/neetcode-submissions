class Solution:
    def isValid(self, s: str) -> bool:
        pairings:dict[str, str] = {"}": "{", ")" : "(", "]": "["}
        stack:list[str] = []

        for char in s:
            if char in pairings.values():
                stack.append(char)
            elif char in pairings.keys() and pairings.get(char) in stack:
                if stack[-1] == pairings.get(char):
                    stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        return False