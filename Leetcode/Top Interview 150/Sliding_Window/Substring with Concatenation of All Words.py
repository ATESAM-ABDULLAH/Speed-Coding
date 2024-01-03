from collections import deque, defaultdict


def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    word_len = len(words[0])  # Calculate length of the first word
    ori_word_dict = defaultdict(int)  # Create dictionary to count words

    for word in words:
        ori_word_dict[word] += 1  # Count occurrences of each word

    all_word_len = len(words) * word_len  # Calculate total word length

    result = []  # Initialize list for resulting indices

    for i in range(word_len):
        queue = deque()  # Initialize queue for encountered words
        word_dict = ori_word_dict.copy()  # Copy the original word dictionary

        for j in range(i, len(s) - word_len + 1, word_len):
            word = s[j : j + word_len]  # Extract substring of length 'word_len'

            if word_dict.get(word, 0) != 0:
                word_dict[word] -= 1  # Decrement word count
                queue.append(word)  # Add word to the queue

                if sum(word_dict.values()) == 0:
                    result.append(
                        j - all_word_len + word_len
                    )  # Add starting index to results
                    last_element = queue.popleft()
                    word_dict[last_element] = word_dict.get(last_element, 0) + 1
            else:
                while len(queue):
                    last_element = (
                        queue.popleft()
                    )  # Remove elements until finding current word
                    if last_element == word:
                        queue.append(word)  # Add current word back to queue
                        break
                    else:
                        word_dict[last_element] = (
                            word_dict.get(last_element, 0) + 1
                        )  # Increment count

                        if word_dict[last_element] > ori_word_dict[last_element]:
                            word_dict = ori_word_dict.copy()  # Reset dictionary

    return result  # Return list of starting indices


s = "ababaab"
words = ["ab", "ba", "ba"]
print(findSubstring(s, words))
