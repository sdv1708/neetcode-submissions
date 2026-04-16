class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(opening, close, path): 
            if opening == n and close == n: 
                result.append("".join(list(path)))
                return 
            
            if opening < n: 
                path.append("(")
                backtrack(opening + 1, close, path)
                path.pop()
            
            if close < opening: 
                path.append(")")
                backtrack(opening, close + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return result
        