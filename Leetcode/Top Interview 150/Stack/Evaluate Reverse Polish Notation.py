from collections import deque


def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = deque()
    for t in tokens:
        if t not in "+-*/":  # Number
            stack.append(int(t))
        else:  # Operator -> pull top 2 nums
            r, l = stack.pop(), stack.pop()
            if t == "+":
                stack.append(l + r)
            elif t == "-":
                stack.append(l - r)
            elif t == "*":
                stack.append(l * r)
            else:
                stack.append(int(float(l) / r))
    return stack.pop()


tokens = ["18"]
print(evalRPN(tokens))
