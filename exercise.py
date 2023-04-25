class Solution:
    def isValid(self, s: str) -> bool:
        symbol = {')': '(', ']': '[', '}': '{'}
        occ = []
        if not s:
            return False
        for i in s:

            if (i in symbol.keys()) and occ.pop() != symbol[i]:
                return False
            elif i in symbol.values():
                occ.append(i)
        if occ:
            return False
        else:
            return True

s="()[]{}"
a = Solution()
b=a.isValid(s)
print(b)