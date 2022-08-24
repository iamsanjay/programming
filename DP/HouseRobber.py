#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:47:17 2022

This is "House Rober" problem, a dynamic programming problem.

I have written three different version of this code 
and all of them are following bottom-top approach.

1. Using a dictinary "rob_1"
2. Using a array "rob_2"
3. Then I have realized that I do not need to remember all the position, I can just use
 two variable and but then I need to perform swap operation on every iteration which
impacted the running time, though reduced the memory usage.  "rob"

@author: sanjaydutt
"""

class Solution(object):
    
    def rob_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dt = {}
        
        dt[0] = nums[0]
        if l == 1:
            return dt[0]
        dt[1] = nums[1] if nums[1] > nums[0] else nums[0]
        if l == 2:          
            return dt[1]
        
        for i in range(2, l):
            dt[i] = max(dt[i-1] , dt[i-2]+nums[i])
        
        return dt[l-1]
    
    def rob_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dt = {}
        
        dt = [0]*l
        dt[0] = nums[0]
        if l == 1:
            return dt[0]
        dt[1] = nums[1] if nums[1] > nums[0] else nums[0]
        if l == 2:
            return dt[1]
        
        for i in range(2, l):
            dt[i] = max(dt[i-1] , dt[i-2]+nums[i])
        
        return dt[l-1]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        
        x1 = nums[0]
        if l == 1:
            return x1
        x2 = nums[1] if nums[1] > nums[0] else nums[0]
        if l == 2:
            return x2
        
        for i in range(2, l):
            temp = x2
            x2 = max(x2 , x1+nums[i])
            x1 = temp
        
        return x2
    
s = Solution()
assert s.rob([1]) == 1
assert s.rob_1([1]) == 1
assert s.rob_2([1]) == 1

assert s.rob([1, 1]) == 1
assert s.rob_1([1, 1]) == 1
assert s.rob_2([1, 1]) == 1

assert s.rob([1, 2]) == 2
assert s.rob_1([1, 2]) == 2
assert s.rob_2([1, 2]) == 2

assert s.rob([1,2,3,1]) == 4
assert s.rob_1([1,2,3,1]) == 4
assert s.rob_2([1,2,3,1]) == 4
