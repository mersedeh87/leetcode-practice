# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/
from __future__ import annotations


def remove_duplicate_letters(s: str) -> str:
    last = {ch: i for i, ch in enumerate(s)}
    stack: list[str] = []
    in_stack = set()

    for i, ch in enumerate(s):
        if ch in in_stack:
            continue

        while stack and stack[-1] > ch and last[stack[-1]] > i:
            in_stack.remove(stack.pop())

        stack.append(ch)
        in_stack.add(ch)

    return "".join(stack)


def _run_tests() -> None:
    tests = [
        ("bcabc", "abc"),
        ("cbacdcbc", "acdb"),
        ("abcd", "abcd"),
    ]
    for s, expected in tests:
        got = remove_duplicate_letters(s)
        if got != expected:
            raise AssertionError(f"FAIL: s={s!r} expected={expected!r} got={got!r}")
    print("All tests passed ")


if __name__ == "__main__":
    _run_tests()