def Distinct(mylist):
    return set(mylist)
  # seen = set()
  # return [x for x in mylist if x not in seen and not seen.add(x)]
print(Distinct([1, 2, 1, 1, 3, 5, 5, 7, 9])) # [1, 2, 3, 5, 7, 9]