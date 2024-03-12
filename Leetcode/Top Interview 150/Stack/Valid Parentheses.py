from collections import deque


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) < 2:
        return False
    stack = deque()
    for i in s:
        if i in "{([":  # opening bracket
            stack.append(i)
        else:  # closing bracket
            if (
                not stack  # stack empty
                or (i == "}" and stack[-1] != "{")  # wrong pairs
                or (i == ")" and stack[-1] != "(")
                or (i == "]" and stack[-1] != "[")
            ):
                return False
            stack.pop()
    return len(stack) == 0


s = "){"
print(isValid(s))
