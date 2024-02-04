def check(func):
    def is_list_sorted(*, lst: list) -> list:
        sorted_list = sorted(lst)
        return sorted_list

    def wrapper(*args, **kwargs):
        sorted_list = is_list_sorted(lst=kwargs['lst'])
        kwargs['sorted_lst'] = sorted_list
        result = func(*args, **kwargs)
        return result

    return wrapper


@check
def bin_search(*, lst: list[int], sorted_lst: list[int], value: int):
    i = 0
    lbound = 0
    ubound = len(sorted_lst) - 1
    while lbound <= ubound:
        i += 1
        mid = ubound + lbound // 2
        mid_value = sorted_lst[mid]
        if mid_value == value:
            return mid_value
        elif value > mid_value:
            lbound = mid + 1
        else:
            ubound = mid - 1
        print(i)
    return -1


print(bin_search(lst=[1, 2, 3, 5, 17, 67, 78, 239, 341], value=5))
numbers = [2, 1, 5, 32, 43, 12, 4, 6]
print(bin_search(lst=numbers, value=12))
num = [-2, 3, 4, 32, -123, 11, 45]
print(bin_search(lst=num, value=32))
print(bin_search(lst=num, value=-2))
