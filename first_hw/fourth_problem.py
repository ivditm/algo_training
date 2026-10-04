def solution(data, R, B) -> int:
    stop = ['R', 'B']
    for fig in R:
        l, c = fig[0], fig[1]
        up = 1
        while l - up >= 0:
            if data[l - up][c] in stop:
                break
            data[l - up][c] = 1
            up += 1
        down = 1
        while l + down <= 7:
            if data[l + down][c] in stop:
                break
            data[l + down][c] = 1
            down += 1
        right = 1
        while c + right <= 7:
            if data[l][c + right] in stop:
                break
            data[l][c + right] = 1
            right += 1
        left = 1
        while c - left >= 0:
            if data[l][c - left] in stop:
                break
            data[l][c - left] = 1
            left += 1
    for fig in B:
        l, c = fig[0], fig[1]
        up_left = 1
        while l - up_left >= 0 and c - up_left >= 0:
            if data[l - up_left][c - up_left] in stop:
                break
            data[l - up_left][c - up_left] = 1
            up_left += 1
        down_right = 1
        while l + down_right <= 7 and c + down_right <= 7:
            if data[l + down_right][c + down_right] in stop:
                break
            data[l + down_right][c + down_right] = 1
            down_right += 1
        up_right = 1
        while l - up_right >= 0 and c + up_right <= 7:
            if data[l - up_right][c + up_right] in stop:
                break
            data[l - up_right][c + up_right] = 1
            up_right += 1
        down_left = 1
        while l + down_left <= 7 and c - down_left >= 0:
            if data[l + down_left][c - down_left] in stop:
                break
            data[l + down_left][c - down_left] = 1
            down_left += 1
    cnt = 0
    for i in range(8):
        for j in range(8):
            if data[i][j] == 1:
                cnt += 1
    return 64 - (cnt + len(R) + len(B))


def lire_data() -> tuple[
           list[list[str]], list[tuple[int]]]:
    data = []
    B = []
    R = []
    for _ in range(8):
        line = input().strip()
        line_to_append = []
        for idx, symbol in enumerate(line):
            if symbol == 'R':
                R.append((_, idx))
            if symbol == 'B':
                B.append((_, idx))
            line_to_append.append(symbol)
        data.append(line_to_append)
    return data, R, B


if __name__ == '__main__':
    print(solution(*lire_data()))
