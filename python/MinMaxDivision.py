K = 3
M = 5
A = [2, 1, 5, 1, 2, 2, 2]


def solution(K, M, A):
    worst_rating_bound = sum(A)
    best_rating_bound = max(A)

    if K == 1:
        return worst_rating_bound

    if K >= len(A):
        return best_rating_bound

    rating = 0
    while worst_rating_bound >= best_rating_bound:
        mid_rating = int((worst_rating_bound + best_rating_bound) / 2)
        need_k = get_k_for_rating(mid_rating, A)
        if need_k > K:
            best_rating_bound = mid_rating + 1
        else:
            worst_rating_bound = mid_rating - 1
            rating = mid_rating

    return rating


def get_k_for_rating(rating, A):
    needed_boxes = 1

    curr_sum = 0
    for i, number in enumerate(A):
        if curr_sum + number > rating:
            needed_boxes += 1
            curr_sum = number
        else:
            curr_sum += number

    return needed_boxes


assert (solution(K, M, A) == 6)
assert (solution(4, M, [0, 0, 0, 0]) == 0)
assert (solution(4, M, [4, 4, 4, 4]) == 4)
assert (solution(4, M, [4, 4, 7, 4]) == 7)
assert (solution(4, M, [1]) == 1)
assert (solution(4, M, [1]) == 1)
assert (solution(1, M, [2, 3]) == 5)
assert (solution(2, M, [1, 2, 1, 2, 1, 2]) == 5)
assert (solution(1, M, [0, 0, 0, 0, 0, 1]) == 1)
assert (solution(2, M, [0, 0, 0, 0, 0, 1]) == 1)
assert (solution(2, M, [0, 0, 0, 0, 1, 1]) == 1)
assert (solution(3, M, [0, 0, 99, 0, 0]) == 99)
assert (solution(2, M, [0, 0, 99, 1, 0]) == 99)
assert (solution(3, M, [0, 1, 99, 1, 0]) == 99)
