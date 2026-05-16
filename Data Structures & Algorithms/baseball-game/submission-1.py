class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        output = 0 
        
        for op in operations: 
            if op not in '+DC':
                stack.append(int(op))
                output += int(op)
            elif op == '+': 
                output += (stack[-1] + stack[-2])
                stack.append(stack[-1] + stack[-2])
            elif op == 'D': 
                output += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif op == 'C': 
                output -= stack.pop()
        
        return output


        