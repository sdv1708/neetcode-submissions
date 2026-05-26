class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] 

        for index, temp in enumerate(temperatures):          
            while stack and stack[-1][1] < temp: 
                stack_i, stack_temp = stack.pop()
                result[stack_i] = (index - stack_i) 

            stack.append((index, temp))
        return result
            