#!/usr/bin/env python3

# CountDiv
#
# Problem taken from codility.com
#
# implementor : Pierre Faivre
# date : 2017-10-18
#
# complexity : between O(1)

import sys


def count_div(A, B, K):
    """Compute number of integers divisible by K in range [A..B]
    """
    ans = 0
    interval = B - A

    # First case, the interval is smaller than K
    if interval < K:
        # We can find a divisible number at most once
        # The difference of the rests tells us if we cross that number during the interval
        if (A % K) > (B % K) or A == 0:
            ans = 1
        else:
            ans = 0

        if A % K == 0 and B % K == 0 and A != 0 and B != 0:
            ans += 1
    
    # The interval is greater than K
    else:
        ans = B // K - A // K

        if A % K == 0:
            ans += 1

    return ans


if __name__ == "__main__":
    integers = list(map(int, sys.stdin.readline().rstrip('\n').split(" ")))

    print(count_div(integers[0], integers[1], integers[2]))
