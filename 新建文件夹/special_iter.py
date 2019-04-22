# 使类可以迭代
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    def __iter__(self):  # 返回一个迭代对象
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):  # 不断调用该迭代对象返回下一个值，知道遇见错误
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 10000:  # 推出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值


for n in Fib():
    print(n)
