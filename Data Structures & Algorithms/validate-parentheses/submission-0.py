class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pair = { ')' : '(', '}':'{', ']': '[' };
        opn = set(pair.values())
        
        for i in s:
            if i in opn:
                stack.append(i)
            elif i not in pair:
                return False
            else:
                if not stack:
                    return False            
                top = stack.pop()
                if top != pair[i]:
                        return False

        if stack:
            return False

        return True

               