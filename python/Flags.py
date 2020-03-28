A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]


# solution can be optimised by using bisection in finding a proper number of flags
# instead of iterating through all of them (even with the stop it can me costly when we can
# put almost all of the flags)
def brute(A):
    peaks = []

    for i in range(1, len(A) - 1):
        prev_node = A[i - 1]
        curr_node = A[i]
        next_node = A[i + 1]

        if curr_node > prev_node and curr_node > next_node:
            peaks.append(i)

    print('BRUTE NUM OF PEAKS: ' + str(len(peaks)))

    max_flags = 0

    for i in range(1, len(peaks) + 1):
        flags_to_put = i
        prev_peak = None
        needed_dist = i

        for j in range(0, len(peaks)):
            if prev_peak is None:
                flags_to_put -= 1
                prev_peak = peaks[j]
                if flags_to_put == 0:
                    break
                else:
                    continue

            curr_peak = peaks[j]
            dist = abs(prev_peak - curr_peak)
            if dist >= needed_dist:
                flags_to_put -= 1
                prev_peak = peaks[j]
                if flags_to_put == 0:
                    break

        if flags_to_put == 0:
            max_flags = i
        else:
            break

    return max_flags


def solution(A):
    peaks = []

    # get peaks
    for i in range(1, len(A) - 1):
        prev_node = A[i - 1]
        curr_node = A[i]
        next_node = A[i + 1]

        if curr_node > prev_node and curr_node > next_node:
            peaks.append(i)

    max_flags = 0

    # check number of flags
    left_side = 1
    right_side = len(peaks)

    while left_side <= right_side:
        i = int((left_side + right_side) / 2)
        flags_to_put = i
        prev_peak = None
        needed_dist = i

        for j in range(0, len(peaks)):
            if prev_peak is None:
                flags_to_put -= 1
                prev_peak = peaks[j]
                if flags_to_put == 0:
                    break
                else:
                    continue

            curr_peak = peaks[j]
            dist = abs(prev_peak - curr_peak)
            if dist >= needed_dist:
                flags_to_put -= 1
                prev_peak = peaks[j]
                if flags_to_put == 0:
                    break

        if flags_to_put == 0:
            max_flags = i

        if flags_to_put > 0:
            # we didn't manage to put all of the flags - take less
            right_side = i - 1
        else:
            # we managed to put all of the flags - take more
            left_side = i + 1

    return max_flags


# assert (solution(A) == 3)
# assert (solution([1, 2, 1]) == 1)
# assert (solution([1]) == 0)
# assert (solution([1, 2]) == 0)
# assert (solution([1, 1, 1, 1]) == 0)
# assert (solution([1, 2, 1, 2, 1]) == 2)

# test1 = [7, 16, 23, 54, 100, 12, 43, 72, 10, 2, 75, 2, 5]
# res1 = brute(test1)
# assert (solution(test1) == res1)

test2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
res2 = brute(test2)
assert (solution(test2) == res2)
