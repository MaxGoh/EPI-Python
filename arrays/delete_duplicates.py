from typing import List


def delete_duplicates(A: List[int]) -> List[int]:
    """
    Time Complexity: O(n)

    :param A: List[int]
    :return: List[int]
    """
    result = []

    for i in A:
        if not result:
            result.append(i)

        else:
            if i != result[-1] and i not in result:
                result.append(i)

    return result


def test():
    result = delete_duplicates([1, 1, 2, 2])
    assert result == [1, 2]
    result = delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13, 2, 2])
    assert result == [2, 3, 5, 7, 11, 13]


def main():
    test()


if __name__ == "__main__":
    main()
