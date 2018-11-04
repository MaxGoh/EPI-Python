from typing import List


def plus_one(A: List[int]) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    :param A: List[int
    :return: List[int]
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break

        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A


def test():
    result = plus_one([1, 2, 9])
    assert result == [1, 3, 0]
    result = plus_one([5, 1, 2])
    assert result == [5, 1, 3]
    result = plus_one([9, 9])
    assert result == [1, 0, 0]
    result = plus_one([9, 9, 9])
    assert result == [1, 0, 0, 0]


def main():
    test()


if __name__ == "__main__":
    main()
