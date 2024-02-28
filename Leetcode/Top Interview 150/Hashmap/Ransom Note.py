def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    i = 0
    while i < len(ransomNote):  # traverse over note
        if ransomNote.count(ransomNote[i]) <= magazine.count(
            ransomNote[i]
        ):  # if letter needed <= letter available: solution possible
            ransomNote = ransomNote.replace(
                ransomNote[i], ""
            )  # remove the letter from note and continue with next
        else:  # letter needed > letter available: not possible
            return False
    return True


ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
