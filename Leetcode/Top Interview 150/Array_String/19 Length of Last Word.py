def lengthOfLastWord(s):
    # # Approach 1: split and len
    # words = [w for w in s.split(" ") if w != ""]
    # return len(words[-1])

    # Approach 2: count letters in reverse until space
    length = 0
    for x in reversed(s):
        if x.isalpha():  # if word found
            length += 1
        elif length:  # if word ended
            break
    return length


string = "   fly me   to   the moon  "
print(lengthOfLastWord(string))
