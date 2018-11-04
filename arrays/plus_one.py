from typing import List


def plus_one(A: List[int]) -> List[int]:
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


if __name__ == "__main__":
    print(plus_one([1, 2, 9]))  # [1, 3, 0]
    print(plus_one([5, 1, 2]))  # [5, 1, 2]
    print(plus_one([9, 9]))  # [1, 0, 0]
    print(plus_one([9]))  # [1, 0, 0]
    print(plus_one([9, 9, 9, 9]))  # [1, 0, 0, 0]
