###import os
###import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    time = s.strip()

    h, m, s = map(int, time[:-2].split(":"))

    p = time[-2:]

    h = h % 12 + (p.upper() == "PM") * 12

    return ("%02d:%02d:%02d") % (h, m, s)


if __name__ == "__main__":
    ###f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    ###f.write(result + '\n')
    print(result + "\n")

    ###f.close()
