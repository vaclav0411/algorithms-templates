# 66243732
from typing import List


ZERO_POS = '0'


def read_input() -> List[int]:
    n = int(input().strip())
    number_list = input().strip().split()
    if len(number_list) != n:
        raise ValueError('Длина списка не соответствует аргументу n')
    return number_list


def find_zero_in(number_list: List[int]) -> List[int]:
    zero = None
    result = []
    for k, v in enumerate(number_list):
        if v == ZERO_POS:
            result.append(0)
            zero = k
        elif zero is not None:
            result.append(k-zero)
        else:
            result.append(len(number_list))
    return result


def nearest_zero(number_list: List[int]) -> List[int]:
    right = find_zero_in(number_list)
    left = find_zero_in(number_list[::-1])[::-1]
    return [min(x) for x in zip(right, left)]


if __name__ == '__main__':
    print(*nearest_zero(read_input()))
