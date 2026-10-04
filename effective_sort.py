# 86698064
from random import randint


class User:

    def __init__(self, username, points, penalty):
        self.__username = username
        self.__points = points
        self.__penalty = penalty

    def __lt__(self, other):
        return (
                (-self.__points, self.__penalty, self.__username) <
                (-other.__points, other.__penalty, other.__username)
            )

    def __str__(self):
        return self.__username


def efficient_quicksort(persons: list, low: int, high: int):

    if low >= high:
        return -1
    left, right = low, high
    pivot = persons[randint(low, high)]
    while left <= right:
        while persons[left] < pivot:
            left += 1
        while persons[right] > pivot:
            right -= 1
        if left <= right:
            persons[left], persons[right] = persons[right], persons[left]
            left += 1
            right -= 1
    efficient_quicksort(persons, low, right)
    efficient_quicksort(persons, left, high)


if __name__ == '__main__':
    number = int(input())
    persons = []
    for index in range(number):
        username, points, penalty = input().split()
        persons.append(
            User(points=int(points), penalty=int(penalty), username=username)
        )
    efficient_quicksort(persons, low=0, high=len(persons)-1)
    print(*persons, sep='\n')
