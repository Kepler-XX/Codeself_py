"""实例001：数字组合
题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析 遍历全部可能，把有重复的剃掉。"""

# 第一种方式
total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if ((i != j) and (j != k) and (k != i)):
                            print(i, j, k)
                            total += 1
print(total)


# 第二种方式
import itertools
sum2 = 0
a = [1, 2, 3, 4]
for i in itertools.permutations(a, 3):
    print(i)
    sum2 += 1
print(sum2)
