class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack and pairing
        pairings:dict[str, str] = {"}": "{", ")" : "(", "]": "["}
        stack:list[str] = []

        for char in s:
            #push to stack if opening bracket
            if char in pairings.values():
                stack.append(char)
            
            #pop stack if last element is the opening counterpart
            elif char in pairings.keys() and pairings.get(char) in stack:
                if stack[-1] == pairings.get(char):
                    stack.pop()
            else:
                return False
        
        #Valid if final stack is empty
        if len(stack) == 0:
            return True
            
        return False