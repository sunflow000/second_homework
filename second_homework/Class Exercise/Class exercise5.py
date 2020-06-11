#1.用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
#定义类XiaoQu
class XiaoQu:
    #说明类变量
    def __init__(self,name,property):
        #类变量name,property
        self.name =name
        self.property = property
        #打印输出的内容
        print("小区名：",name,"小区物业：",property)
#定义子类GdangXqu，并继承类XiaoQu
class GdangXqu(XiaoQu):
    #　继承类的变量
    def __init__(self,name,property):
        # 　继承类的构造方法
        super().__init__(name,property)
        # 　创建方法huan_jing，输入参数flower
    def huan_jing(self,flower):
        # 　判断如果flower参数为None,输出“小区没有花”
        if flower is None:
            print("小区里没有花")
        # 　判断如果flower非None，输出“小区里有{}花".format(flower),"环境好”
        else:
            print("小区里有{}".format(flower),"环境好")
#实例化类
c = GdangXqu("阳光新天地","万科物业")
#实例化类方法huan_jing，并给参数赋值
c.huan_jing(None)