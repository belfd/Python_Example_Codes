# Python pass argument by object reference (not by value and not by reference)

def set_list(list):
    list = ["A", "B", "C"]  # here a new assignment will create object
    return list


def add(list):
    list.append("D") # here we use the original object to extend its value
    return list


my_list = ["E"]
print(f"id of my_list: {id(my_list)}")
x1 = set_list(my_list)
x2 = add(my_list)
print(f"id of my_list is {id(x1)} and value is: {x1}")
print(f"id of my_list is {id(x2)} and value is: {x2}")