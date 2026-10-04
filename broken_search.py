# 86692910

def broken_search(nums: list, target: int) -> int:
    """
    Функция выполняет бинарный поиск в сломанном массиве
    для поиска индекса целевого элемента.

    Возвращает:
    - целое число, представляющее индекс целевого элемента, если он найден,
     в противном случае -1
    """

    if not nums:  # если массив пустой
        return -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6.


test()
