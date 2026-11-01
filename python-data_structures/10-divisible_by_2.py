def divisible_by_2(my_list=[]):
    new_list = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            new_list[num] = True
        elif my_list[num] % 2 != 0:
            new_list[num] = False
    return new_list