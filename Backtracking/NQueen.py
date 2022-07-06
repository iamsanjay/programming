#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 08:04:24 2022

@author: sanjaydutt

In this specific program I find issue with my Stack which I was thinking of copying from other program that 
I wrote yesterday. But I was admant on typing it again and writing new test cases while I was doin that I find a new issue with my Stack.
Overall Testing ROCKS!!!
"""

class Stack:
    def __init__(self, n):
        self.size = n
        self.arr = [None]*n
        self.top = -1
    def pop(self):
        if self.top == -1:
            raise Exception("Underflow")
        x = self.arr[self.top]
        self.top -= 1
        return x
    def push(self, x):
        if self.top == self.size-1:
            raise Exception("Overflow")
        self.top += 1
        self.arr[self.top] = x
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def head(self):
        if self.top == -1:
            return None
        return self.arr[self.top]
    def lis(self):
        l=[] 
        for i in range(0, self.top+1):
            l.append(self.arr[i])
        return l
print("============ Testing for Stack starts here ===================")

s1 = Stack(5)
s1.push(5)
s1.push(5)
s1.push(5)
s1.push(5)
s1.push(5)
try:
    s1.push(5)
except:
    print("Adding over limit i.e. Overflow")

assert s1.pop() == 5
assert s1.pop() == 5
assert s1.pop() == 5
assert s1.pop() == 5
assert s1.pop() == 5


s1 = Stack(0)
try:
    s1.pop()
except:
    print("It was expected")
try:
    s1.push(10)
except:
    print("This also expected as size is 0")

s1 = Stack(1)
ele = 10
s1.push(ele)
assert s1.top == 0
assert s1.pop() == ele

s1.push(10)
try:
    s1.push(20)
except:
    print("Yes expected!!")
print("============ Testing for Stack ends here ===================")

def queen_placed_or_removed(x, y , n, m, placed = True):
    """
    This method will place or remove queen from (x,y) along with marking other 
    position according whether they are available or not.
    Status 1 means yes they are available
    Status 2 means nope it's not available
    """
    status = 1 
    if not placed:
        status = -1
    m[x][y] = m[x][y] + status
    for i in range(y+1, n+1): # Moving along the columns (Forward direction).
        m[x][i] = m[x][i] + status
    
    x1 = x-1
    y1 = y+1
    while x1 > 0 and y1 < n+1: # Moving diagonally, row decreasing and col increasing. 
        m[x1][y1] = m[x1][y1] + status
        x1 -= 1
        y1 += 1

    x1 = x+1
    y1 = y+1
    while x1 < n+1 and y1 < n+1: # Moving diagonally, row increasing and col increasing too.
        m[x1][y1] = m[x1][y1] + status
        x1 += 1
        y1 += 1

print("============ Testing for queen_placed_or_removed starts here ===================")
m = [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,1],
     [1,1,1,1]]
n = len(m)
queen_placed_or_removed(2, 2, n-1,m)
print(m)
assert m[2][2] == 2
assert m[2][3] == 2
assert m[1][3] == 2
assert m[3][3] == 2
assert sum([sum(i) for i in m]) == 20
queen_placed_or_removed(2, 2, n-1,m, False)
assert m[2][2] == 1
assert m[2][3] == 1
assert m[1][3] == 1
assert m[3][3] == 1
assert sum([sum(i) for i in m]) == 16
m = [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,1],
     [1,1,1,1]]
n = len(m)
queen_placed_or_removed(1, 1, n-1,m)
assert sum([sum(i) for i in m]) == 21
print("============ Testing for queen_placed_or_removed ends here ===================")

def next_jump(x, y, n, m):
    options = []
    for i in range(1, n+1):
        if m[i][y+1] == 1:
            options.append([i, y+1])
    return options

print("============ Testing for next_jump starts here ===================") 
m = [[1,1,1,1],
     [1,2,2,2],
     [1,1,2,1],
     [1,1,1,2]]
n = len(m)
options = next_jump(1, 1, n-1, m)
assert len(options) == 1
assert options[0] == [3, 2]

m = [[1,1,1,1],
     [1,1,2,1],
     [1,2,2,2],
     [1,1,2,1]]
n = len(m)

options = next_jump(2, 1, n-1, m)
assert len(options) == 0

m = [[1,1,1,1],
     [1,1,1,2],
     [1,1,2,1],
     [1,2,2,2]]
n = len(m)
options = next_jump(3, 1, n-1, m)
assert len(options) == 1
assert options[0] == [1,2]
print("============ Testing for next_jump ends here ===================")

def nQueen(n):
    if n == 1:
        return [1]
    ans = []
    for i in range(1, n+1):
        s1 = Stack(n-1)
        s2 = Stack(n)
        s1.push([i,1])
        s2.push(i)
        m = [[1]*(n+1) for i in range(n+1)]
        queen_placed_or_removed(i, 1, n, m)
        dict={}
        while not s1.isEmpty():
            [x,y] = s1.head()
            options = next_jump(x, y, n, m)
            str_coord = str(x)+""+str(y)
            if str_coord not in dict:
                dict[str_coord] = 0
            visited_count = dict[str_coord]
            if visited_count == len(options):
                s1.pop()
                s2.pop()
                dict[str_coord] = 0
                queen_placed_or_removed(x, y, n, m, placed=False)
                continue
            dict[str_coord] = dict[str_coord] + 1
            [x1, y1] = options[visited_count]
            if y1 == n:
                l = s2.lis()
                l.append(x1)
                ans.append(l)
                continue
            s1.push([x1, y1])
            s2.push(x1)
            queen_placed_or_removed(x1, y1, n, m)
    return ans
print("============ Testing for nQueen starts here ===================")

print(nQueen(6))
assert len(nQueen(1)) == 1
assert len(nQueen(2)) == 0
assert len(nQueen(4)) == 2
print("============ Testing for nQueen ends here ===================")



