def solution(need_space: list[int]) -> int:
    s = 0
    for i in need_space:
        tabs = i // 4
        space = i % 4
        if space >= 3:
            s += tabs + 2
        else:
            s += tabs + space
    return s


if __name__ == '__main__':
    num_ligne = int(input())
    need_space = [int(input()) for _ in range(num_ligne)]
    print(solution(need_space))
