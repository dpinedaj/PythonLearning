"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, 
and an encoded message, count the number of ways it can be decoded.

For example, the message '111' 
would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. 
For example, '001' is not allowed.
"""

MAPPING = {str(i): chr(i + 96) for i in range(1, 27)}
CHOICES = [1, 2]


def problem7(encoded: str) -> str:
    encoded_length: int = len(encoded)
    possibilities: list = []

    def loop_sum(acc: list) -> None:
        if sum(acc) == encoded_length:
            possibilities.append(acc)
        elif sum(acc) < encoded_length:
            for val in CHOICES:
                loop_sum(acc + [val])

    loop_sum([])
    print(possibilities)
    result = [
        [MAPPING.get(encoded[i : i + val]) for i, val in enumerate(pos)]
        for pos in possibilities
    ]
    return ["".join(res) for res in result if None not in res]


test = "1111"
problem7(test)
