"""

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = [""] * numRows
        row = 0
        next_row = False

        if numRows == 1:
            return s

        for i in s:
            ret[row] += i
            if row == 0 or row == numRows - 1:
                next_row = not next_row
            row += 1 if next_row else - 1

        return ''.join(ret)


s = "AB"
numRows = 1
Solution().convert(s, numRows)

"""
0P 4A 8H 12N
1A 3P 5L 7S 9I 11I 13G
2Y 6I 10R

"""