class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        unaccounted = []
        for a in s:
            if a in '[({':
                stack.append(a)
            else:
                if a == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                elif a == ']' and len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                elif a == '}' and len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    unaccounted.append(a)
        return (len(stack) == 0 and len(unaccounted) == 0)