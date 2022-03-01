mylist = [10,12,36,[41,59,63],[77],81,93]
flat = []
for i in mylist:
 if isinstance(i, list):
   flat.extend(i) #add all the elements in list in one iteration
 else:
   flat.append(i) #add single element
print(flat) #output: [10, 12, 36, 41, 59, 63, 77, 81, 93]