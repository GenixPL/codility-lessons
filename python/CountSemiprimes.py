import math

N = 26
P = [1, 4, 16]
Q = [26, 10, 20]

# BRUTE

# I will use a system in which each index corresponds to the same value - A[0] holds value for 0, etc


def solution(N, P, Q):
    queries = []

    semi_primes = get_semi_primes_up_to(N)

    num_of_primes_till = [0] * (N + 1)
    for i in range(1, len(num_of_primes_till)):
        num_of_primes_till[i] = num_of_primes_till[i - 1] + semi_primes[i]

    for k in range(len(P)):
        p_k = P[k]
        q_k = Q[k]

        queries.append(num_of_primes_till[q_k] - num_of_primes_till[p_k - 1])

    return queries


def get_primes_up_to(N):
    # prepare table for primes
    is_prime_list = [True] * (N + 1)
    # mark 0 and 1 as non-prime
    is_prime_list[0] = False
    is_prime_list[1] = False

    for a in range(2, N + 1):
        # skip non-primes
        if not a:
            continue

        # mark non-primes
        # we can skip checking up to square of a given number
        for non_prime in range(a ** 2, N + 1, a):
            is_prime_list[non_prime] = False

    return is_prime_list


def get_semi_primes_up_to(N):
    is_prime_list = get_primes_up_to(math.ceil(N / 2))

    semi_primes = [False] * (N + 1)
    for i in range(len(is_prime_list)):
        if not is_prime_list[i]:
            continue

        value = i ** 2
        if value <= N:
            semi_primes[value] = True
        else:
            break

        for j in range(i + 1, len(is_prime_list)):
            if not is_prime_list[j]:
                continue

            value = i * j
            if value <= N:
                semi_primes[value] = True
            else:
                break

    return semi_primes


# PROPER SOLUTION


assert (solution(N, P, Q) == [10, 4, 0])
print(solution(50000, [1] * 30000, [50000] * 30000))
assert (solution(1, [1, 1], [1, 1]) == [0, 0])
