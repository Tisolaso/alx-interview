#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    triangle = []

    if n <= 0:
        return []

    for i in range(1, n + 1):
        new = []
        for y in range(0, i):
            if y == 0 or y == i - 1:
                new.append(1)
            else:
                old = triangle[i-2]
                new.append(old[y - 1] + old[y])
        
        triangle.append(new)
    
    return triangle