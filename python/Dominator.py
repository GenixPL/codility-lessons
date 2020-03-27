from math import floor

A = [3, 4, 3, 2, 3, -1, 3, 3]


def solution(A):
    # return -1 when there is no dominator

    # check if array is empty
    if not A:
        return -1

    sorted_a = sorted(A)
    has_dominator = False
    last_element = sorted_a[0]
    counter = 0

    for element in sorted_a:
        if last_element == element:
            counter += 1
            if counter > len(A) / 2:
                has_dominator = True
                break
        else:
            if counter > len(A) / 2:
                has_dominator = True
                break
            else:
                counter = 1
                last_element = element

    if has_dominator:
        for i, element in enumerate(A):
            if element == last_element:
                return i
    else:
        return -1


assert (solution(A) == 0)
assert (solution([]) == -1)
assert (solution([1, 2]) == -1)
assert (solution([1, 1, 1]) == 0)
assert (solution([1, 2, 2]) == 1)
assert (solution([1, 1, 2, 2, 3]) == -1)
assert (solution([1, 1, 2, 2, 3, 3, 3]) == -1)
assert (solution([2, 1, 2, 1, 2]) == 0)
assert (solution([2, 2, 2, 2, 2, 4, 4, 4, 4, 4]) == -1)
assert (solution([2, 1, 1, 3]) == -1)

