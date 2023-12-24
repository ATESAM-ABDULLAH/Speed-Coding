def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # List of letters/nums in string
    s = [l for l in s.lower() if l.isalnum()]
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
