A = [15, 10, 3]
B = [75, 30, 5]

def solution(A, B):
    count = 0

    for x, y in zip(A, B):
        if has_same_prime_divisors(x, y):
            count += 1

    return count


def has_same_prime_divisors(x, y):
    gcd_value = gcd(x, y)  # The gcd contains all the common prime divisors

    x = remove_common_prime_divisors(x, gcd_value)

    if x != 1:
        # If x and y have exactly the same common prime divisors, x must be composed by
        # the prime divisors in gcd_value. So after previous loop, x must be one.
        return False

    y = remove_common_prime_divisors(y, gcd_value)

    return y == 1


def gcd(x, y):
    # Compute the greatest common divisor.
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def remove_common_prime_divisors(x, y):
    # Remove all prime divisors of x, which also exist in y. And return the remaining part of x.

    while x != 1:
        gcd_value = gcd(x, y)
        if gcd_value == 1:
            # x does not contain any more common prime divisors
            break
        x /= gcd_value

    return x






assert (solution(A, B) == 1)
# assert (solution([6059, 551], [442307, 303601]) == ?)
