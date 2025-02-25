def add_to_list(lst, item):
    lst[item] = None
    return list(lst.keys())


lst = {}
lst[1] = None
lst[2] = None
lst[2] = None 
lst[3] = None
print(add_to_list(lst, 3))  