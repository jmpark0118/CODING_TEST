import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a, n):

    count = 0
    flag = 1
    while flag:
        flag = False
        for i in range(1, n):
            if a[i-1]>a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                count += 1
                flag = True
        if flag == False:
            break

    print('Array is sorted in', count, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a, n)
