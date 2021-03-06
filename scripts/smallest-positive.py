print('Print smallest positive in list using Solution 1')


def smallest_positive_1(in_list):
    # print(in_list)
    # Sort the list
    in_list.sort()
    # print list before finding positive number
    # print(in_list)
    # smallest_positive = ""
    smallest_pos = None
    for num in in_list:
        if num > 0:
            return num
    return smallest_pos


# Call smallest_positive(in_list) to print the lowest number in the list
print(smallest_positive_1([4, -6, 7, 2, -4, 10]))
print(smallest_positive_1([7, 3, -9, -1, 4]))
print(smallest_positive_1([-9, -8, -4, -21, -6]))


print('Print smallest positive in list using Solution 2')
def smallest_positive_2(in_list):
    #print list before sorting
    print(in_list)
    smallest_pos = None
    for num in in_list:
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

print(smallest_positive_2([4, -6, 7, 3, -4, 10]))
