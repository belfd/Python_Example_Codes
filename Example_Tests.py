def change(my_list):
   my_list.append(5)
   return my_list

my_list = [10, 20]
print(change(my_list))
print(my_list)
# Output:
# [10, 20, 5]
# [10, 20, 5]