def removeDuplicateLetters(s:str)-> str:
    last_index ={ch:i for i, ch in enumerate(s)}
    stack =[]
    seen =set()
    for i ,ch in enumerate(s):
        if ch not in seen:
            while stack and ch < stack[-1] and i < last_index[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
    return ''.join(stack)

def _run_tests():
    test_cases = [
        ("bcabc", "abc"),
        ("cbacdcbc", "acdb"),
        ("abacb", "abc"),
        ("bbcaac", "bac"),
    ]
    for s, expected in test_cases:
        result = removeDuplicateLetters(s)
        assert result == expected, f"Test failed for input {s}: expected {expected}, got {result}"
    print("All tests passed.")