'''13. Print the First n Rows of Pascal's Triangle

Write a Python function that prints out the first n rows of Pascal's triangle.

Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

Sample Pascal's triangle : Python exercise solutions
                            1
                          1   1
                        1   2  1
                    1    3   3   1
                1     4    6   4   1
                    
Pascal's triangle
Each number is the two numbers above it added together
'''
def pascal(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row=[l + r for l, r in zip(row +y, y+row)]
    return n >= 1
pascal(6)
        


