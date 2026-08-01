class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                if token == "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif token == "-":
                    second_token = stack.pop()
                    first_token = stack.pop()
                    stack.append(int(first_token) - int(second_token))
                elif token == "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif token == "/":
                    second_token = stack.pop()
                    first_token = stack.pop()
                    stack.append(int(int(first_token) / int(second_token)))

        return int(stack[0]) if stack else 0
                