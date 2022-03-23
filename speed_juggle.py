# 66246379
from typing import List


COUNT_ITER = 4


def read_input() -> List[int]:
    k = int(input().strip())
    number_list = [input().strip() for _ in range(COUNT_ITER)]
    combine_list = ''.join(number_list)
    return k, combine_list


def juggle(k: int, number_list: List[int]) -> int:
    list_clear = [int(x) for x in number_list if x not in '.']
    set_number = set(list_clear)
    point = sum([1 for x in set_number if list_clear.count(x) <= 2 * k])
    return point


if __name__ == '__main__':
    print(juggle(*read_input()))
