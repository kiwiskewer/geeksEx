import operator, re
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}

class Solution(object):
    def diffWaysToCompute(self, s):
        nums = [int(x) for x in re.findall(r'[0-9]+', s)]
        opers = re.findall(r'\+|\-|\*', s)
        n, DP = len(nums), {}
        for i in range(n):
            DP[i, i] = [nums[i]]
        for i in range(n - 1):
            DP[i, i+1] = [ops[opers[i]](nums[i], nums[i + 1])]
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                DP[i, j] = []
                for v in range(i, j):
                    left = DP[i, v]
                    right = DP[v + 1, j]
                    for e1 in left:
                        for e2 in right:
                            DP[i, j].append(ops[opers[v]](e1, e2))
        return DP[0, n - 1]
    def diffWaysToCompute1(self, input):
        tokens = re.split('(\D)', input)
        nums = list(map(int, tokens[::2]))
        ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2]))
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b)
                    for i in range(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]
        return build(0, len(nums) - 1)

sol = Solution()
print (sol.diffWaysToCompute('1+1+1+1'))
print (sol.diffWaysToCompute1('1+1+1+1'))
