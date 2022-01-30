n = int(input())


def permutation(arr: list):
    """
    """
    if len(arr) == 1:
        return [arr]

    perm_list = []
    for el_arr in arr:
        remaining_elements = [x for x in arr if x != el_arr]
        sub_arr = permutation(remaining_elements) # permutations of sublist

        for el_sub_arr in sub_arr:
            perm_list.append([el_arr] + el_sub_arr)

    return perm_list


def print_result(perms_array: list):
    """
    """
    print(len(perms_array))
    for arr in perms_array:
        print(' '.join(list(map(str, arr))))
    

permutations_array = permutation([x for x in range(1, n + 1)])

print_result(permutations_array)
