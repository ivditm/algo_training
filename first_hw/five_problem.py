# не проходит лимит по времени
def find_profit(n, k, d):
    x = n
    for _ in range(d):
        x *= 10
        for chiffre in range(10):
            a = x + chiffre
            if a % k == 0:
                x = a
                break
        else:
            return -1
    return x


if __name__ == '__main__':
    data = input().split()
    n, k, d = int(data[0]), int(data[1]), int(data[2])
    print(find_profit(n, k, d))
