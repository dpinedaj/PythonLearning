def solution(s):
    c = s[0]
    if c.isupper():  # please fix condition
        return "upper"
    elif c.islower():  # please fix condition
        return "lower"
    elif c.isdigit():  # please fix condition
        return "digit"
    else:
        return "other"


if __name__ == "__main__":
    print(solution("1ola"))
