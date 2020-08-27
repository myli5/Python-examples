"""
Q6. word Avg - Write a function that takes a string input
  and determine the average length of words.
Time complexity: O(n) n is number of words
Space complexity: O(1)
"""
def avgWordLength(s) -> float:
    words = s.split(" ")
    length, count = 0, 0
    for word in words:
        if word:
            length += len(word)
            count += 1
    if count == 0:
        return None
    return length / count

assert avgWordLength("Hello world!")  == 5.5