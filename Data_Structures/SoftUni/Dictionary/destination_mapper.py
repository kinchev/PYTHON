# import re
#
# # text = input()
#
# pattern = r'(=|\/){1}([A-Z][A-Za-z]{2,})(\1)'
#
# # x = [x[1] for x in re.findall(pattern, text)]
# #
# # y=sum([len(x[1]) for x in re.findall(pattern, text)])
#
# print(f"Destinations: {', '.join([x[1] for x in re.findall(pattern, input())])}\nTravel Points: {sum([len(x[1]) for x in re.findall(pattern, input())])}")

import sys


# array = list(map(int, input().split((','))))
# print(array)


def solution(A):
    max = sys.minsize
    max1 = 0
    for n in A:
        if n <= 0:
            print(0)
        elif n > 0 and n > max:
            max1 = n
            print(max1)


A = [1, 3, 4, 6]


# 1,3,6,4,1,2


# def solution(A)
#
    # that, given an
#1 1 2 3 4 6
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# # Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unau
