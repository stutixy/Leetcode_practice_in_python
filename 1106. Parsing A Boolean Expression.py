class Solution:
    def parseBoolExpr(self, exp: str) -> bool:

        def converttobool(s):
            if s == "t":
                return True
            return False

        def converttostr(s):
            if s == True:
                return "t"
            return "f"

        stack = [] # (operator or bool)
        operator = set(["&", "|", "!"])
        values = set(["t", "f"])
        
        for r in range(len(exp)):
            if exp[r] in operator:
                stack.append(exp[r])
            elif exp[r] in values: 
                if stack and stack[-1] in values:
                    top = converttobool(stack.pop())
                    curr = converttobool(exp[r])
                    if stack[-1] == "&":
                        stack.append(converttostr(top and curr))
                    elif stack[-1] == "|":
                        stack.append(converttostr(top or curr))
                else:
                    stack.append(exp[r])
                
            elif exp[r] == ")":
                q = deque()
                while stack and stack[-1] in values:
                    q.append(converttobool(stack.pop()))
                op = stack.pop()
                
                if op == "&":
                    stack.append(converttostr(all(q)))
                elif op == "|":
                    stack.append(converttostr(any(q)))
                elif op == "!":
                    top = not q.popleft()
                    stack.append(converttostr(top))
        res = converttobool(stack.pop())
        return res
                
                

                







  