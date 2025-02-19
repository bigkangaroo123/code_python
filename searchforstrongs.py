from collections import Counter


def solve(needle, haystack):
    n, h = len(needle), len(haystack)

    if n > h:
        return 0
    
    sorted_n = sorted(needle)
    counter = 0

    for i in range((h-n)+1):
        sorted_part = sorted(haystack[i:i+n])
        if sorted_part == sorted_n:
            counter += 1

    return counter

needle = input()
haystack = input()

print(solve(needle, haystack))