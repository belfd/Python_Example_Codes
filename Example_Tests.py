from itertools import chain

li = ['ABC', 'DEF', 'GHI', 'JKL']
# using chain-single iterable.
res1 = list(chain(li))
res2 = list(chain.from_iterable(li))
print("using chain :", res1, end ="\n\n")  # output: ['ABC', 'DEF', 'GHI', 'JKL']
print("using chain.from_iterable :", res2) # output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']



