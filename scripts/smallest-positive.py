print('Print smallest positive in list using Solution 1')

def smallest_positive_1(in_list):
    print(in_list)
    #Sort the list
    in_list.sort()
    #print list before finding positive number
    print(in_list)
    #smallest_positive = ""
    smallest_pos = None
    for num in in_list:
        if num > 0:
            return num
    return smallest_pos

#Call smallest_positive(in_list) to print the lowest number in the list
print(smallest_positive_1([4, -6, 7, 2, -4, 10]))
print(smallest_positive_1([7,3,-9,-1,4]))



