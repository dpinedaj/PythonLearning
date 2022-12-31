# #
# # abc*+ is a+b*c [parenthesis is not required]
# # abc/+* is invalid


def post_to_in(string):
    stack = []
    for k in string:
        if k in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            new_entry = a + k + b
            stack.append("(" + new_entry + ")")
        else:
            stack.append(k)
    return new_entry


print(post_to_in("abc/+*"))
