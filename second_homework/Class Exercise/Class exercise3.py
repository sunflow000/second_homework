#1.用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
#定义类Dog
class Dog:
    # 定义构造函数,定义变量name
    def __init__(self,name):
        # 变量为name
        self.name = name
    #     定义方法open，并传参
    def open(self,a):
        # 输出打开的实施者
        print(self.name,"，打开")
        a.open()
    # 定义方法close
    def close(self,b):
        # 输出关闭的实施者
        print(self.name,"，关上")
        b.close()

# 定义类box
class Box:
    # 定义构造函数，函数变量name
    def __init__(self,name):
        self.name = name
    #    定义类方法open
    def open(self):
        # 输出打开的物品
        print(self.name,"打开了")
    #     定义类方法close
    def close(self):
        # 输出关闭的物品
        print(self.name,"关上了")


#实例化类
D = Dog("大黄")
B = Box("箱子")
# 实例化类的方法open,close
D.open(B)
# B.open()
D.close(B)
# B.close()




