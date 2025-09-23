class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(" , "}" : "{" , "]" : "[" }

        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                                                                        # Runtime: 0ms // Beats 100%
        return True if not stack else False                             # Memory : 17.92 MB // Beats 34.32%
