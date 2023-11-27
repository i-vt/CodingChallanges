"""
6. Zigzag Conversion
Medium
7K
13.7K
Companies

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

 

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000


"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #1:50 - 2:55, about 10 reruns lol
        # the top one will always be in array 0
        # bottom one will be in array n-1 ( letter)
        # horizontal len will be n-2
        # horizontal are in reverse order b/c coming from bottom to up


        if numRows == 1 or len(s) == 1 or numRows > len(s): return s
        if numRows == 2:
            top = ""
            bottom = ""
            switch = False
            for i in s:
                if switch: 
                    bottom += i
                    switch = False
                else:
                    top += i
                    switch = True
            return top + bottom
        down = []
        horizontal = []
        matrix = []
        rtrn = ""
        iteration_size = numRows+numRows-2
        # 14 letters / (4+4-2) = 2.33
        # 14L / (3+3-2) = 3.5
        #iterations
        import math
        iterations = math.ceil(len(s)/iteration_size)
        list1 = list(range(numRows))
        list2 = list1[::-1][1:-1]
        matrix_filling_pattern = []
        for i in list1: matrix_filling_pattern.append(i)
        for i in list2: matrix_filling_pattern.append(i)
        #matrix_filling_pattern = [range(numRows), range(numRows)[::-1][1:-1]]
        print(matrix_filling_pattern)

        
        for _ in range(numRows): matrix.append("")
        for i in range(iterations):
            for j in range(len(matrix_filling_pattern)):
                if s == "": break
                matrix[matrix_filling_pattern[j]] += s[0]
                s = s[1:]

            if s == "": break
        
        rtrn = ""
        for i in matrix: rtrn += i

        return rtrn
