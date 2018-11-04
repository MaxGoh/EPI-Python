from typing import List


def multiply(A: List[int], B: List[int]) -> List[int]:
    """
    Time Complexity: O(nm)

    :param A: List[int]
    :param B: List[int]
    :return: List[int]
    """
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])

    result = [0] * (len(A) + len(B))

    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            result[i + j + 1] += A[i] * B[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + + 1] %= 10

    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    result[0] *= sign
    return result


def test():
    result = multiply([2], [3])
    assert result == [6]
    result = multiply([-1, 2, 3], [1, 2, 3])
    assert result == [-1, 5, 1, 2, 9]
    result = multiply([5, 2, 3], [3, 2, 1])
    assert result == [1, 6, 7, 8, 8, 3]


def main():
    test()


if __name__ == "__main__":
    main()
