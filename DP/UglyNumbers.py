#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 15:51:02 2022

@author: sanjaydutt
"""

class Solution:
    def uglyNum(self, N):
        # code here
        ctr = 2
        num = 1
        dict={}
        dict[1] = True
        while ctr <= N:
            k = 0
            num = num + 1
            if num % 2 == 0:
                k = int(num/2)
            elif num % 3 == 0:
                k = int(num/3)
            elif num % 5 == 0:
                k = int(num/5)
            if k in dict:
                dict[num] = dict[k]
            else:
                dict[num] = False
            if dict[num]:
                ctr = ctr + 1
        return num
s = Solution()


assert s.uglyNum(1) == 1
assert s.uglyNum(2) == 2
assert s.uglyNum(7) == 8
assert s.uglyNum(10) == 12
assert s.uglyNum(15) == 24
assert s.uglyNum(150) == 5832

