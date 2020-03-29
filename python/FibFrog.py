A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]


# N = 0
# 0, 1, 0, 1, ...
# 0, 0, 0, ..., 1 - only one jump
# 1, 1, 1, 1 - with best score == 1
# check empty
# 0, 0, 0, 0, ...


def solution(A):
    A.append(1)  # add value for last point - opposite riverbank
    fib_numbers = get_fib_numbers_up_to(26)  # there are 26 fib numbers less than 100 000

    need_jumps_list = [-1] * len(A)

    # mark those leaves that can be reached with one jump
    for fib_num in fib_numbers:
        if fib_num > len(A):
            break

        if A[fib_num - 1] == 1:
            need_jumps_list[fib_num - 1] = 1

    # go through each leaf
    for i in range(len(A)):
        # skip non-leaves and those that can be reached with one jump
        if A[i] == 0 or need_jumps_list[i] == 1:
            continue

        can_be_reached = False
        best_needed_jumps = 100001

        # go through each possible possible jump
        for jump in fib_numbers:
            # get index of previous leaf for given jump
            prev_leaf_i = i - jump

            # check if previous leaf for such jump can exist
            if prev_leaf_i < 0:
                break

            # check if this leaf can be reached somehow
            if A[prev_leaf_i] == 0 or need_jumps_list[prev_leaf_i] < 0:
                continue  # skip this jump if it cannot be performed

            # if jump will produce better score than current, then remember it
            if best_needed_jumps > need_jumps_list[prev_leaf_i] + 1:
                best_needed_jumps = need_jumps_list[prev_leaf_i] + 1
                can_be_reached = True

        if can_be_reached:
            need_jumps_list[i] = best_needed_jumps

    return need_jumps_list[len(A) - 1]


def get_fib_numbers_up_to(n):
    fib_nums = [0] * n

    fib_nums[0] = 0
    fib_nums[1] = 1

    for i in range(2, n):
        fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]

    fib_nums.pop(0)  # we can remove 0, since it will not produce any jumps
    fib_nums.pop(0)  # we can remove one 1, since it is duplicated

    return fib_nums


# assert (solution(A) == 3)
assert (solution([0, 0, 0, 0]) == 1)
# assert (solution([0, 0, 0]) == -1)
assert (solution([]) == 1)
