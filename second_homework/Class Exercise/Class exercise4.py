#1.用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
# 定义类手机
class Phone:
    #创建构造函数，说明类变量
    def __init__(self,brand,model,color):
        #类变量品牌，型号，颜色
        self.brand = brand
        self.model = model
        self.color = color
    #创建类的买的方法
    def buy(self):
        #判断品牌，如果品牌是华为且颜色是红色
        if self.brand =="华为" and self.color=="red":
            # 输出＂买买买＂
            print("买买买")
        #     如果品牌是三星
        elif self.brand =="三星":
            # 输出＂再看看＂
            print("再看看")
        #     如果品牌是其他的，输出＂不买了＂
        else:
            print("不买了")

# 实例化看到的一个手机
myphone = Phone(brand="华为",model="A7511",color="red")
# 实例化方法
myphone.buy()
