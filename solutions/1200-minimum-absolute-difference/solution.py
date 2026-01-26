from typing import List


def minimum_abs_difference(arr: List[int]) -> List[List[int]]:
    arr.sort()

    min_diff = float("inf")
    res: List[List[int]] = []

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]

        if diff < min_diff:
            min_diff = diff
            res = [[arr[i], arr[i + 1]]]
        elif diff == min_diff:
            res.append([arr[i], arr[i + 1]])

    return res


def _run_tests() -> None:
    tests = [
        ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
        ([1, 3, 6, 10, 15], [[1, 3]]),
        ([3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]]),
    ]

    for arr, expected in tests:
        got = minimum_abs_difference(arr)
        if got != expected:
            raise AssertionError(f"FAIL: arr={arr} expected={expected} got={got}")

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()