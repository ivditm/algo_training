def solution(numbers: list[int]) -> str:
    operators = ''
    f = numbers[0]
    for s in numbers[1:]:
        if (s % 2 != 0) and (f % 2 != 0):
            operators += 'x'
            f *= s
        else:
            operators += '+'
            f += s
    return operators


if __name__ == '__main__':
    n = int(input())
    numbers = [int(_) for _ in input().split()]
    print(solution(numbers))
