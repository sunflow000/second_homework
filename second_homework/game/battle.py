#     定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
#
#     see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，
#     如果传入“丁春秋”，打印“叛徒！我杀了你”
#     fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
#     进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
#

# 希望各位同学在此基础上可以添加自己的“freestyle”哦
class TongLao():
    def __init__(self,blood,power):  #构造函数，说明类的变量

        # 类变量血量
        self.blood = blood
        # 类变量攻击力
        self.power = power
    def see_people(self,name1):        #定义类方法see_people
        # 判断看到的人是无崖子
        if name1=="无崖子":
            # 输出“师弟”
            print(name1,"师弟")
            #判断看到的人是李秋水　　　　　　　
        elif name1=="李秋水":
            # 输出“贱人”
            print(name1,"贱人！")
            # 判断看到的人是丁春秋
        elif name1 =="丁春秋":
            # 输出“叛徒，我要杀了你”

            print(name1,"叛徒,我要杀了你")

    # 定义天山折梅手方法，并需要传入敌人血量，敌人攻击力
    def fight_zms(self,emblood,empower):
        blood = self.blood/2                 #TongLao血量减两倍
        power = self.power *10               #TongLao攻击力涨10倍
        print("我的剩余血量：",self.blood-empower-blood)           #输出TongLao血量
        print("敌人的剩余血量：",emblood-self.power-power)             #输出敌人血量
        if (self.blood -blood-empower) > (emblood-self.power-power): #打架，如果TongLao血量大于敌人

            print("我赢了，高兴！") #输出赢了的内容
        elif (self.blood-blood-empower) < (emblood-self.power-power):
            print("敌人赢了，沮丧")  #输出输了的内容
        else:
            print("平局，再战一回合")  #输出平局的内容



c = TongLao(300,5)  #实例化类
c.see_people("无崖子") #实例化方法see_people
c.fight_zms(200,2)  #实例化方法fight_zms


