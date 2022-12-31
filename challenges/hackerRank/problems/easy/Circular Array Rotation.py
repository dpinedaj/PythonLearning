"""John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the value of the element at a given index.

For example, array , number of rotations,  and indices to check, .
First we perform the two rotations:

Now return the values from the zero-based indices  and  as indicated in the  array.


Function Description

Complete the circularArrayRotation function in the editor below. It should return an array of integers representing the values at the specified indices.

circularArrayRotation has the following parameter(s):

a: an array of integers to rotate
k: an integer, the rotation count
queries: an array of integers, the indices to report"""


# Complete the circularArrayRotation function below.
import collections


def circularArrayRotation(a, k, queries):
    d = collections.deque(a)
    d.rotate(k)
    return (d[i] for i in queries)


if __name__ == "__main__":
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print("\n".join(map(str, result)))
    print("\n")
