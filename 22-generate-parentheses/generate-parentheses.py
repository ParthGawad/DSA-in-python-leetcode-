class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [],[] 
        
        def dfs(openn, closen) : 
            # if the number of open & close parenthesis are equal to the n, then format & return the result
            if openn == closen == n :
                res.append("".join(stack))
                return

            # if the number of open paranthesis is less than the n, then add the ( & recursive call the function with incremented openn value, after the recursion, pop the top value to backtrack to the previous solution, same logic goes to )
            if openn < n :
                stack.append("(")
                dfs(openn + 1, closen)
                stack.pop()

            if closen < openn :
                stack.append(")")
                dfs(openn, closen + 1)
                stack.pop()

        dfs(0,0)
        return res
# Time complexity : O(2**n)
# Space complexity : O(n)