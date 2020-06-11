#1.用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
#创建一个学生类
class Student:
    #定义构造函数，说明类变量，方便实例化的时候对类变量赋值
    def __init__(self,name,sex,age):
        #类变量姓名
        self.name = name
        # 类变量性别
        self.sex =sex
        # 类变量年龄
        self.age =age
     #创建一个方法：上课，参数为分数
    def shang_ke(self,score1):
        # 输出上课分数
        print("上课得分:{}".format(score1))
       #创建考试方法，参数为分数
    def exam(self,score2):
        # 赋值输出考试成绩
        print("考试成绩是：{}".format(score2))


#定义一个子类EStudent，继承Student
class EStudent(Student):
    #继承Student变量
    def __init__(self,name,sex,age):
        # 继承Student的构造方法
        super().__init__(name,sex,age)
       # 输出姓名，性别，年龄
        print("姓名：",self.name,"性别：",self.sex,"年龄：",self.age)
    #     创建方法逃课，参数为分数score3
    def truancy(self,score3):
        # 赋值输出逃课扣分
        print("逃课扣分：{}".format(score3))

#实例化学生类
c = EStudent("xiaoming","男",15)
# 实例化方法：　上课，考试，逃课，并赋值
c.shang_ke(10)
c.exam(80)
c.truancy(5)


