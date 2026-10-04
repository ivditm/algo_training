def solution(p: int, v: int, q: int, m: int) -> int:
    if (p + v) < (q - m) or (q + m) < (p - v):
        return 2 * v + 1 + 2 * m + 1
    elif (q - m) <= (p - v) and (p + v) <= (q + m):
        return 2 * m + 1
    elif (q - m) >= (p - v) and (p + v) >= (q + m):
        return 2 * v + 1
    else:
        if (p - v) <= (q + m) and (p + v) >= (q + m):
            return (p + v) - (q - m) + 1
        else:
            return (q + m) - (p - v) + 1


if __name__ == '__main__':
    p_v = input()
    q_m = input()
    print(solution(int(p_v.split()[0]),
                   int(p_v.split()[1]),
                   int(q_m.split()[0]),
                   int(q_m.split()[1])))
