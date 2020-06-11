#1.用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
#定义person 类
class Person:
    #定义1个方法run，同时传入km参数
    def run(self,km):
    # 输出“我能跑”
        print("我能跑{}公里".format(km))
    #定义1个方法eat
    def eat(self,number):
    # 输出“我能吃”
        print("我能吃馒头{}个".format(number))
#实例化类变量mike
mike = Person()
#传入mike跑的公里数
mike.run(2)
#继承Person类，EPerson
class Eperson(Person):
#定义Eperson的方法jump
    def jump(self,cm):
     #输出“我能跳的高度”，并传入cm参数
        print("我能跳{}cm高".format(cm))
#实例化类lucy
lucy = Eperson()
#调用继承Person类的方法eat
lucy.eat(5)
#调用Eperson本身的方法jump
lucy.jump(50)


