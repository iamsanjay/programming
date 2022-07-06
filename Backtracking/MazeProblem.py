#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:22:03 2022

@author: sanjaydutt

This problem available at https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1 
"""
class Stack:
    def __init__(self, size):
        self.arr = [None]*size
        self.size = size
        self.top = -1
    def pop(self):
        if self.top == -1:
            raise Exception("Underflow")
        x = self.arr[self.top]
        self.top -= 1
        return x
    def push(self, x):
        if self.top == self.size:
            raise Exception("Overflow")
        self.top += 1
        self.arr[self.top] = x
    def head(self):
        if self.top == -1:
            return None
        return self.arr[self.top]
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def path(self):
        list = []
        for i in range(0, self.top+1):
            list.append(self.arr[i])
        return  ''.join(list)
    
s1 = Stack(0)
# I am not really sure, How to test exception in Python?
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

s1 = Stack(10)
s1.push('A')
s1.push('B')
s1.push('C')
assert s1.path() == 'ABC'


def next_jump(x,y, m, n):
    move_x = [1, 0, 0, -1]
    move_y = [0,-1, 1, 0]
    options = []
    dire = 'DLRU'
    for i in range(0, 4):
        x1 = x + move_x[i]
        y1 = y + move_y[i]
        if x1 < 0 or x1 > n-1 or y1 < 0 or y1 > n-1: # Out of grid
            continue
        if m[x1][y1] == 2 or m[x1][y1] == 0: # Either visted or blocked
            continue
        options.append(([x1, y1], dire[i]))
    return options



m=[[1, 0, 0, 0],
   [1, 1, 0, 1], 
   [1, 1, 0, 0],
   [0, 1, 1, 1]]
assert len(next_jump(3, 3, m, len(m))) == 1
assert len(next_jump(1, 2, m, len(m))) == 2
assert len(next_jump(3, 2, m, len(m))) == 2

m=[[0, 1, 0, 0],
   [1, 1, 1, 0], 
   [0, 1, 0, 0],
   [0, 0, 0, 0]]
assert len(next_jump(1,1,m,len(m))) == 4

m = [[1]]
assert len(next_jump(0,0,m,len(m))) == 0
assert len(next_jump(1,1,m,len(m))) == 0

m = [[0,1],[1,0]]

assert len(next_jump(0, 1, m, len(m))) == 0
assert len(next_jump(1, 0, m, len(m))) == 0

def maze(m,n):
    s = Stack(n*n)
    s1 = Stack(n*n-1)
    path = []
    dict = {}
    if m[0][0] == 0:
        return []
    m[0][0] = 2
    s.push([0,0])
    while not s.isEmpty():
        [x, y] = s.head()
        options = next_jump(x, y, m, n)
        str_cord = str(x)+""+str(y)
        print("Start", [x, y])
        if str_cord not in dict:
            dict[str_cord] = 0
        visited_count = dict[str_cord]
        print("Visited_Count", visited_count, [x,y], options)
        if visited_count == len(options):
            print("Entered", [x,y])
            s.pop()
            if not s1.isEmpty():
                s1.pop()
            dict[str_cord] = 0
            m[x][y] = 1
            continue
        dict[str_cord] = dict[str_cord] + 1
        [x1, y1], d = options[visited_count]
        if [x1, y1] == [n-1, n-1]:
            print("YES")
            path.append(s1.path()+d)
            continue
        s.push([x1, y1])
        s1.push(d)
        m[x1][y1] = 2
    return path


m = [ [ 1, 0, 0, 0, 0 ],
      [ 1, 1, 1, 1, 1 ],
      [ 1, 1, 1, 0, 1 ],
      [ 0, 0, 0, 0, 1 ],
      [ 0, 0, 0, 0, 1 ] ]
n = 5
print(maze(m,n))