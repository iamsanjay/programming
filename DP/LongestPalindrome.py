#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:57:16 2022

@author: sanjaydutt
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        cbbd 
        
        
        
        SRTBOT    
            Subproblem :- s[i, j] is the longest substring in a string starting at i and ending at j
            Relate :-  s[i, j] = i == j + s[i-1 , j-1]
            Topological Order :- We are increasing the length of String in each iteration starting from i = 1 to n
            Base case :- j - i <= 1 return True
            Time :- I am not going to analyze this today, for sure!!!
            
            Example
            
            ABCDEFGHI

            Bottom-up approach
            
            Stage 1
            AB (1,2)
            BC (2,3)
            CD (3,4)
            DE (4,5)
            EF (5,6)
            FG (6,7)
            GH (7,8)
            HI (8,9)
            EF (4,5)
            GH (5,6)
            IJ (6,7)
            
            Stage 2
            ABC (1,3)
            BCD (2,4)
            CDE (3,5)
            DEF (4,6)
            EFG (5,7)
            FGH (6,8)
            GHI (7,9)
            
            Stage 3
            ABCD (1,4) = (1 == 4 + s[23])
            BCDE (2,5) = (2 == 5 + s[34])
            CDEF (3,6) = (3 == 6 + s[45])
            DEFG (4,7) = (4 == 5 + s[56])
            EFGH (5,8) = (5 == 8 + s[67])
            FGHI (6,9) = (6 == 9 + s[78])
            
            Stage 4
            ABCDE (1,5) = (1 == 5 + s[2,4])
            BCDEF (2,6) = (2 == 6 + s[3,5])
            CDEFG (3,7) = (3 == 7 + s[4,6])
            DEFGH (4,8) = (4 == 8 + s[5,7])
            EFGHI (5,9) = (5 == 9 + s[6,8])
            
            Stage 5
            ABCDEF (1,6) = (1 == 6 + s[2,5])
            BCDEFG (2,7) = (2 == 7 + s[3,6])
            CDEFGH (3,8) = (3 == 8 + s[4,7])
            DEFGHI (4,9) = (4 == 9 + s[5,8])
            
            Stage 6
            ABCDEFG (1,7) = (1 == 7 + s[2,6])
            BCDEFGH (2,8) = (2 == 8 + s[3,7]) 
            CDEFGHI (3,9) = (3 == 9 + s[4,8])
            
            Stage 7
            ABCDEFGH (1,8) = (1 == 8 + s[2,7])
            BCDEFGHI (2,9) = (2 == 9 + s[2,8])
            
            Stage 8 
            ABCDEFGHI (1,9) = (1 == 9 + s[2,8])
            
            
            
            |1,1|1,2|1,3|1,4|1,5|1,6|1,7|1,8|1,9|
            |   |2,2|2,3|2,4|2,5|2,6|2,7|2,8|2,9|
            |   |   |3,3|3,4|3,5|3,6|3,7|3,8|3,9|
            |   |   |   |4,4|4,5|4,6|4,7|4,8|4,9|
            |   |   |   |   |5,5|5,6|5,7|5,8|5,9|
            |   |   |   |   |   |6,6|6,7|6,8|6,9|
            |   |   |   |   |   |   |7,7|7,8|7,9|
            |   |   |   |   |   |   |   |8,8|8,9|
            |   |   |   |   |   |   |   |   |9,9|

        """
        
        l = len(s)
        
        mat = [[0]*(l) for _ in range(l)]
        for i in range(0, l):
            mat[i][i] = 1

        ptr = 1
        largI = 0
        largJ = 0
        for _ in range(0,l-1):
            i = 0
            j = ptr
            while j < l:
                
                if s[i] == s[j] and (i+1 > j-1 or mat[i+1][j-1] == 1):
                    mat[i][j] = 1
                    largI = i
                    largJ = j
                
                j = j + 1
                i = i + 1
            ptr = ptr + 1
        
        if largI == largJ:
            return s[0]
        else:
            return s[largI: largJ + 1]
                
            
s = Solution()

# Single char
assert s.longestPalindrome("A") == "A"

# Two char diff
assert s.longestPalindrome("AB") == "A"

# Two Char same
assert s.longestPalindrome("AA") == "AA"

# three char palindrome            
assert s.longestPalindrome("ABA") == "ABA"

# All char unique
assert s.longestPalindrome("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "A"        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        