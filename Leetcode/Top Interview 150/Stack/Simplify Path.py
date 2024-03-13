from collections import deque


def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    stack = deque()
    path = path.split("/")  # split into directories
    for p in path:
        if p != "" and p != ".":  # ignore the '/' and '.'
            if p == "..":
                if stack:  # go up a level
                    stack.pop()
            else:  # new dir
                stack.append(p)

    return "/" + "/".join(stack)


path = "/../"
print(simplifyPath(path))
