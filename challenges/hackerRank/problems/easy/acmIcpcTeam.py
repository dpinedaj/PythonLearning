# Reference: https://www.hackerrank.com/challenges/acm-icpc-team/problem


def acm_icp_team(data):
    options = [
        sum([int(x) or int(y) for x, y in zip(data[i], data[j])])
        for i in range(len(data))
        for j in range(i + 1, len(data))
    ]

    return (max(options), options.count(max(options)))


data = ["10101", "11110", "00010"]
print(acm_icp_team(data))
