def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]

    1) Do not split words
    2) Try to fit as many words as possible in line
    3) Left-justify: 1 word on line, last line
    4) Fully-justify other lines except (2)
    """
    # Store full para, store a line, store no space chars in line
    para, line, line_char_len = [], [], 0

    for i, w in enumerate(words):
        # Cannot add word to line -> move to new line
        if line_char_len + len(w) + len(line) > maxWidth:
            # Full-Justify line
            for i in range(maxWidth - line_char_len):  # num of spaces to add
                space_slots = max(
                    1, len(line) - 1
                )  # Max (1,min_required_spaces): if 1 word in line
                index = i % space_slots  # index = space % word_before_space
                line[index] += " "

            para.append("".join(line))  # append line to para
            line, line_char_len = [], 0  # reset line, line char count

        # Can word to line
        line_char_len += len(w)  # increase chars in list
        line.append(w)  # add word to line

    line = " ".join(line).ljust(maxWidth)  # Left-justify last line
    para.append(line)  # append last line to para

    return para


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16

print(fullJustify(words, maxWidth))
