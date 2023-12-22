def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s = s.split() # split into words by space
    return " ".join(reversed(s)) # join seperated by space


line = """python3 "/home/atesam/Documents/Leetcode/21 Reverse Words in a String.py"""
print(reverseWords(line))
