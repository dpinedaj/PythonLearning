s = "BANANA"
vowels = "AEIOU"
ready = list()
stuartsc = 0
kevinsc = 0

for i in range(len(s)):
    if s[i] not in vowels and s[i] not in ready:
        for j in range(i, len(s)):
            print(s[i : j + 1], s.count(s[i : j + 1]))
            stuartsc += s.count(s[i : j + 1])
        ready.append(s[i])

    if s[i] in vowels and s[i] not in ready:
        for j in range(i, len(s)):
            print(s[i : j + 1], s.count(s[i : j + 1]))
            kevinsc += s.count(s[i : j + 1])

        ready.append(s[i])

if kevinsc > stuartsc:
    print("Kevin", kevinsc)
elif kevinsc < stuartsc:
    print("Stuart", stuartsc)
else:
    print("Draw")
