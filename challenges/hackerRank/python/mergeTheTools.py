def merge_the_tools(s, k):
    strings = [s[i : i + k] for i in range(0, len(s) - k + 1, k)]
    result = list()
    for i in strings:
        lista = list()
        for j in i:
            if j not in lista:
                lista.append(j)
        result.append("".join(lista))

    return result


s = "AABCAAADA"
k = 3

print(merge_the_tools(s, k))
