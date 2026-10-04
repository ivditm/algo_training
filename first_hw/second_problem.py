def solution(g_1_1: int, g_2_1: int, g_1_2: int, g_2_2: int, i: int) -> int:
    G_1, G_2 = (g_1_1 + g_1_2), (g_2_1 + g_2_2)
    if G_1 > G_2 or (G_1 == G_2 and i == 2 and g_1_1 > g_2_2):
        return 0
    elif i == 1:
        if G_2 == G_1 and g_1_2 == g_2_1:
            return 1
        elif G_2 - G_1 + g_1_2 <= g_2_1:
            return G_2 - G_1 + 1
        else:
            return G_2 - G_1
    else:
        if G_1 == G_2 and g_1_1 == g_2_2:
            return 1
        elif G_2 - G_1 + g_1_2 < g_2_2:
            return G_2 - G_1
        return G_2 - G_1 + 1


if __name__ == '__main__':
    first_line = input().split(':')
    g_1_1, g_2_1 = int(first_line[0]), int(first_line[1])
    second_line = input().split(':')
    g_1_2, g_2_2 = int(second_line[0]), int(second_line[1])
    i = int(input())
    print(solution(g_1_1, g_2_1, g_1_2, g_2_2, i))
