from first_problem import solution


def test_1(func):
    assert func(0, 7, 12, 5) == 25, f'test 1 failed res: {func(0, 7, 12, 5)}'
    print('test 1 ok')


def test_2(func):
    assert func(1, 2, 6, 2) == 10, f'test 2 failed res: {func(1, 2, 6, 2)}'
    print('test 2 ok')


def test_3(func):
    assert func(6, 2, 1, 2) == 10, f'test 3 failed res: {func(6, 2, 1, 2)}'
    print('test 3 ok')


def test_4(func):
    assert func(0, 12, 0, 5) == 25, f'test 4 failed res: {func(0, 12, 0, 5)}'
    print('test 4 ok')


def test_5(func):
    assert func(0, 5, 0, 12) == 25, f'test 5 failed res: {func(0, 5, 0, 12)}'
    print('test 5 ok')


def test_6(func):
    assert func(0, 3, -3, 3) == 10, f'test 6 failed res: {func(0, 3, -3, 3)}'
    print('test 6 ok')


def test_7(func):
    assert func(-3, 3, 0, 3) == 10, f'test 7 failed res: {func(-3, 3, 0, 3)}'
    print('test 7 ok')


def test_8(func):
    assert func(0, 3, 0, 3) == 7, f'test 8 failed res: {func(0, 3, 0, 3)}'
    print('test 8 ok')


def test_9(func):
    assert func(-2, 2, -1, 1) == 5, f'test 9 failed res {func(-2, 2, -1, 1)}'
    print('test 9 ok')


if __name__ == '__main__':
    test_1(solution)
    test_2(solution)
    test_3(solution)
    test_4(solution)
    test_5(solution)
    test_6(solution)
    test_7(solution)
    test_8(solution)
    test_9(solution)
