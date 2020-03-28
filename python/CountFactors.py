import math

N = 24


def brute(N):
    left_value = 1
    right_value = N

    factors = []

    while left_value <= right_value:
        if left_value == right_value:
            if left_value * left_value == N:
                factors.append(left_value)
                break

        value = left_value * right_value

        if value == N:
            factors += [left_value, right_value]
            left_value += 1
            right_value -= 1
            continue

        if value > N:
            right_value -= 1
            continue

        if value < N:
            left_value += 1
            continue

    return len(factors)


def solution(N):
    factors_counter = 2  # we can obviously skip 1 and N

    sq_root = int(math.sqrt(N))

    for i in range(2, sq_root + 1):  # +1 because we want to include this root
        if N % i == 0:
            factors_counter += 2

    # and in case where sq_root is a factorial, then we remove one results, to eliminate repetition
    if sq_root ** 2 == N:
        factors_counter -= 1

    return factors_counter


# assert (solution(N) == 8)
assert (solution(144) == 15)
assert (solution(1) == 1)
assert (solution(2147483647) == 2)
assert (solution(9) == 3)
