#!/usr/bin/env python3

# MinAvgTwoSlice
#
# implementor : Pierre Faivre
# date : 2018-11-20
#
# complexity : O(n)

import sys


def min_avg_two_slice(A):
    minAvg = (A[0] + A[1]) / 2
    minAvgIndex = 0
    avg = 0

    for i, n in enumerate(A[:-2]):
        # Search for a 3-element slice
        avg = (A[i] + A[i+1] + A[i+2]) / 3
        if minAvg > avg:
            minAvg = avg
            minAvgIndex = i

        # Search for a 2-element slice
        avg = (A[i] + A[i+1]) / 2
        if minAvg > avg:
            minAvg = avg
            minAvgIndex = i

        # No need to search for a bigger slice because it would be inevitably 
        # composed of lower average 2 or 3-element slices

    avg = (A[-2] + A[-1]) / 2
    if minAvg > avg:
        minAvg = avg
        minAvgIndex = len(A) - 2

    return minAvgIndex


if __name__ == "__main__":
    user_input = sys.stdin.readline().rstrip('\n')
    user_input = [int(n) for n in user_input.split(' ')]

    print(min_avg_two_slice(user_input))
