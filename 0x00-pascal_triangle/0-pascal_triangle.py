#!/usr/bin/python3

"""
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal's triangle of n
"""

def pascal_triangle(n=0):

    """returns a list of lists of integers representing the Pascal's
    triangle of n

    Args:
        n (integer): number of rows

    Returns:
        list: integers representing Pascal's triangle.
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
