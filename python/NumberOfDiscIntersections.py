
a = [1, 5, 2, 1, 4, 0]


def solution(A):
    events = []

    for i, a in enumerate(A):
        events += [(i - a, 1)]
        events += [(i + a, -1)]

    events.sort(key=lambda x: (x[0], -x[1]))

    open_circles = 0
    iterations = 0

    for _, value in events:
        if value == 1:
            iterations += open_circles

        open_circles += value

        if iterations > 10000000:
            return -1

    return iterations


print(solution(a))
