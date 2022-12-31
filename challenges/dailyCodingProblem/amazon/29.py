"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""


def problem29(text: str, prev: str = "", acc: int = 1, final: str = "") -> str:
    if text == "":
        return final
    else:
        if prev == "":
            pass
        elif prev == text[0]:
            problem29(text[1::], text[0], acc + 1, final)
        else:
            final = final + str(acc) + prev
            problem29(text[1::], text[0], 1, final)


problem29("AAAABBBCCDAA")


text = ""
text[1]
