class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # T- O(n), S- O(n)
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
                
        return stack[0] #single value result that is gauranteed in the stack i.e at index 0