def remove_duplicates(a_list):
    new_list = []
    for i in a_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

list1 = ['a','a','b','c','c','d','e']
new_list1 = remove_duplicates(list1)
print(new_list1)


def remove_duplicates_easier(a_list):
    new_list = []
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(new_list1)

def square(x):
    if x < 0 or x > 10:
        return 'Error'
    elif type(x) != int:
        return 'Error'
    else:
        return x * x
