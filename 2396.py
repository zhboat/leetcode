"""如果一个整数 n 在 b 进制下（b 为 2 到 n - 2 之间的所有整数）对应的字符串 全部 都是 回文的 ，那么我们称这个数 n 是 严格回文 的。

给你一个整数 n ，如果 n 是 严格回文 的，请返回 true ，否则返回 false 。

如果一个字符串从前往后读和从后往前读完全相同，那么这个字符串是 回文的 。

 """


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def calc_base(n):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-=_+[]{}|;:',.<>/?`~"
            for i in range(2, n - 1):
                cacl_num = n
                result = ""
                while cacl_num > 0:
                    result = digits[cacl_num % i] + result
                    cacl_num //= i
                if result != result[::-1]:
                    return False
                else:
                    result = ""
                    continue

        return False if calc_base(n) == False else True


ret = Solution().isStrictlyPalindromic(9)
print(ret)
