A = [3, 2, 6, -1, 4, 5, -1, 2]


def solution(A):
    # we care about slices between <1, n - 1)
    max_slices_from_left = [0] * len(A)
    max_slices_from_right = [0] * len(A)


    # IMPORTANT!!!
    # we get max of current slice and 0, because 0 is chosen only in case when max slice is
    # lower than 0 (obviously), but it's better, in this situation, to move X/Z to this position,
    # in order to receive 0 not something negative

    # get left slices by simulating different positions of Y
    for i in range(1, len(A) - 1):
        max_slices_from_left[i] = max(max_slices_from_left[i - 1] + A[i], 0)

    # get right slices by simulating different positions of Y
    for i in range(len(A) - 2, 0, -1):
        max_slices_from_right[i] = max(max_slices_from_right[i + 1] + A[i], 0)

    max_total = 0
    for i in range(1, len(A) - 1):
        max_total = max(max_slices_from_left[i - 1] + max_slices_from_right[i + 1], max_total)

    return max_total


assert (solution(A) == 17)
assert (solution([5, 5, 5]) == 0)
assert (solution([0, 0, 0, 0, 0]) == 0)
assert (solution([1, 1, 1, 1, 1]) == 2)
assert (solution([1, 1, 0, 10, -100, 10, 0]) == 21)
assert (solution([0, 10, -5, -2, 0]) == 10)
assert (solution([5, 17, 0, 3]) == 17)
assert (solution([5, 0, 17, 3]) == 17)
assert (solution([5, 3, 0, 17]) == 3)
