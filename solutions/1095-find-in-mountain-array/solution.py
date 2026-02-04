from __future__ import annotations


class MountainArray:
    """
    LeetCode provides this interface.
    Locally we mock it for testing.
    """
    def get(self, index: int) -> int:
        raise NotImplementedError

    def length(self) -> int:
        raise NotImplementedError


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:
        n = mountain_arr.length()

        # 1) Find peak index with binary search
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        # 2) Binary search on increasing part [0..peak]
        idx = self._bin_search(mountain_arr, 0, peak, target, asc=True)
        if idx != -1:
            return idx

        # 3) Binary search on decreasing part [peak+1..n-1]
        return self._bin_search(mountain_arr, peak + 1, n - 1, target, asc=False)

    def _bin_search(
        self,
        arr: MountainArray,
        lo: int,
        hi: int,
        target: int,
        asc: bool,
    ) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            val = arr.get(mid)

            if val == target:
                return mid

            if asc:
                if val < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                # descending
                if val < target:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1


# ---------------- Local test harness ---------------- #

class MockMountainArray(MountainArray):
    def __init__(self, data: list[int]):
        self.data = data
        self.calls = 0

    def get(self, index: int) -> int:
        self.calls += 1
        return self.data[index]

    def length(self) -> int:
        return len(self.data)


def _run_tests() -> None:
    sol = Solution()

    tests = [
        # example-ish cases
        (([1, 2, 3, 4, 5, 3, 1], 3), 2),   # first occurrence index of 3 is 2
        (([0, 1, 2, 4, 2, 1], 3), -1),
        (([0, 5, 3, 1], 1), 3),

        # edge-ish
        (([1, 3, 5, 4, 2], 5), 2),         # target is peak
        (([1, 3, 5, 4, 2], 1), 0),         # target at start
        (([1, 3, 5, 4, 2], 2), 4),         # target at end
    ]

    for (arr_list, target), expected in tests:
        m = MockMountainArray(arr_list)
        got = sol.findInMountainArray(target, m)
        if got != expected:
            raise AssertionError(
                f"FAIL: arr={arr_list} target={target} expected={expected} got={got}"
            )

    print("All tests passed ")


if __name__ == "__main__":
    _run_tests()