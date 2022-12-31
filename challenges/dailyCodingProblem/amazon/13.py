"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, 
find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb".
"""


def problem13(text: str, k: int) -> str:
    text_length: int = len(text)
    combinations: list = [
        text[i:j]
        for i in range(text_length)
        for j in range(text_length, -1, -1)
        if len(set(text[i:j])) == k
    ]
    return max(combinations, key=len)


problem13("abcba", 2)
