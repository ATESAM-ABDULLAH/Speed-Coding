from ast import Num
from collections import deque


def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    cur, ans, stack = 0, 0, deque()
    sign = 1  # 1 = +, -1 = -

    for ss in s:
        if ss.isdigit():  # Number
            cur = int(ss) + (10 * cur)  # concat multi digits
        elif ss in "+-":  # Sign
            ans += sign * cur  # running result: res = res + (sign * cur int)
            cur = 0  # refresh cur int
            sign = 1 if ss == "+" else -1
        elif ss == "(":  # Store res, sign outside ()
            stack.append(ans)  # store old result
            stack.append(sign)  # store old sign
            sign, ans = 1, 0  # refresh both
        elif ss == ")":
            ans += sign * cur  # running result inside (): res = res + (sign * cur int)
            old_sign, old_ans = stack.pop(), stack.pop()
            ans = (ans * old_sign) + old_ans  # result inside + result outside
            cur = 0  # refresh cur int
    return ans + (cur * sign)  # res = res + last int


s = " 2-(1 + 2)"
print(calculate(s))
