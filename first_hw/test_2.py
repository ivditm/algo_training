from second_problem import solution


def test_1(func):
    assert func(0, 0, 0, 0, 1) == 1, f'test 1 failed res: {func(0, 0, 0, 0)}'
    print('test 1 ok')


def test_2(func):
    assert func(0, 2, 0, 3, 1) == 5, f'test 2 failed res: {func(0, 0, 0, 0)}'
    print('test 2 ok')


def test_3(func):
    assert func(0, 2, 0, 3, 2) == 6, f'test 3 failed res: {func(0, 0, 0, 0)}'
    print('test 3 ok')


def test_4(func):
    assert func(1, 0, 1, 0, 1) == 0, f'test 4 failed res: {func(0, 0, 0, 0)}'
    print('test 4 ok')


def test_5(func):
    assert func(
        2, 2, 1, 1, 1) == 1, f'test 5 failed res: {func(2, 2, 1, 1, 1)}'
    print('test 5 ok')


def test_6(func):
    assert func(
        2, 2, 1, 1, 2) == 0, f'test 6 failed res: {func(2, 2, 1, 1, 2)}'
    print('test 6 ok')


def test_7(func):
    assert func(1, 0, 1, 1, 1) == 0, f'test 7 failed res {func(1, 0, 1, 1, 1)}'
    print('test 7 ok')


def test_8(func):
    assert func(
        2, 2, 0, 5, 2
        ) == 6, f'test 8 failed res: {func(2, 2, 0, 5, 2)}'
    print('test 8 ok')


def test_9(func):
    assert func(
        1, 2, 3, 4, 2
        ) == 3, f'test 9 failed res: {func(2, 2, 0, 5, 2)}'
    print('test 9 ok')


def test_10(func):
    assert func(
        1, 2, 3, 4, 1
        ) == 2, f'test 10 failed res: {func(2, 2, 0, 5, 1)}'
    print('test 10 ok')


def test_11(func):
    assert func(1, 1, 1, 1, 2) == 1, f'test 11 failed: {func(1, 1, 1, 1, 2)}'
    print('test 11 ok')


def test_12(func):
    assert func(1, 1, 1, 1, 1) == 1, f'test 12 failed: {func(1, 1, 1, 1, 1)}'
    print('test 12 ok')


def test_13(func):
    assert func(5, 2, 0, 5, 1) == 3, f'test 13 failed: {func(5, 2, 0, 5, 1)}'
    print('test 13 ok')


def test_14(func):
    assert func(4, 1, 2, 3, 1) == 0, f'test 14 failed: {func(4, 1, 2, 3, 1)}'
    print('test 14 ok')


def test_15(func):
    assert func(4, 3, 0, 3, 2) == 2, f'test 15 failed: {func(4, 3, 0, 3, 2)}'
    print('test 15 ok')


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
    test_10(solution)
    test_11(solution)
    test_12(solution)
    test_13(solution)
    test_14(solution)
    test_15(solution)
