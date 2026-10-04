from th_problem import solution


def test_1(func):
    assert func(
        [1, 4, 12, 9, 0]
        ) == 8, f'test 1 failed: {func([1, 4, 12, 9, 0])}'
    print('test 1 done')


def test_2(func):
    assert func(
        [0, 0, 0, 0, 0]
        ) == 0, f'test 2 failed {func([0, 0, 0, 0, 0])}'
    print('test 2 done')


def test_3(func):
    assert func(
        [8, 9, 10, 11, 12]
    ) == 16, f'test 3 failed {func([8, 9, 10, 11, 12])}'
    print('test 3 done')


if __name__ == '__main__':
    test_1(solution)
    test_2(solution)
    test_3(solution)
