s_good = '{[()()]}'
s_bad = '([)()]'


def solution(S):
    # check if string is empty
    if not S:
        return 1

    stack = []

    for char in S:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
            continue

        # check is stack is empty
        if not stack:
            return 0

        popped = stack.pop()
        if char == ')' and popped != '(':
            return 0
        if char == '}' and popped != '{':
            return 0
        if char == ']' and popped != '[':
            return 0

    # check if stack is empty
    if not stack:
        return 1
    else:
        return 0


assert (solution('(((') == 0)
assert (solution(')))') == 0)
assert (solution('[[[') == 0)
assert (solution(']]]') == 0)
assert (solution('{{{') == 0)
assert (solution('}}}') == 0)
assert (solution('') == 1)
assert (solution('()') == 1)
assert (solution('[]') == 1)
assert (solution('{}') == 1)
assert (solution('()()') == 1)
assert (solution('[][]') == 1)
assert (solution('{}{}') == 1)
assert (solution('{[]()}([])') == 1)
assert (solution('{[]()}[(])') == 0)
assert (solution('{[](}') == 0)
