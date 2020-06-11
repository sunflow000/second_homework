#     定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
#     加入模块化改造

from second_homework.game.battle import TongLao  #导入TongLao类

class XuZhu(TongLao): #继承TongLao类

    def read(self):   # 新增red 方法
        print("罪过罪过")  # 输出red方法内容

#实例化xuzhu
xuzhu = XuZhu(500,5)
#实例化read方法
xuzhu.read()