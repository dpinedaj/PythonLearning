import math


def viralAdvertising(n):
    share = 5
    liked = 0
    cumulative = 0
    for i in range(n):
        liked = math.floor(share / 2)
        cumulative = cumulative + liked
        share = liked * 3
    return cumulative


if __name__ == "__main__":

    n = int(input())

    result = viralAdvertising(n)
