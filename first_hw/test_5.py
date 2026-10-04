from five_problem import find_profit


def test_1(func):
    assert func(21, 108, 1) == 216, f'test 1 failed: {func(21, 108, 1)}'
    print('test 1 ok')


def test_2(func):
    assert func(5, 12, 4) == -1, f'test 2 failed {func(5, 12, 4)}'
    print('test 2 ok')


if __name__ == '__main__':
    test_1(find_profit)
    test_2(find_profit)
