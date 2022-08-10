# Deep Flatten 
def deep_flatten(inp):
    if len(inp) == 0:
        return inp
    if isinstance(inp[0], list):
        return deep_flatten(inp[0]) + deep_flatten(inp[1:])
    return inp[:1] + deep_flatten(inp[1:])


def deep_flatten(lst):
    return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, list) else [lst])

print(deep_flatten([1, 2, [3, 5, [34, 56]], [23]]))  # [1, 2, 3, 5, 34, 56, 23]
