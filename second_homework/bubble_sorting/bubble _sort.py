# 定义排序的方法
def bubble_sort(list):
    for i in range(len(list)-1):               # 进行i-1次循环比较，i是list的长度

        print(list)#输出列表
        for j in range(len(list)-1-i):          # j 代表列表第j位索引，进行j-1次两两对比循环
            print("第{}次排序".format(i))         # 输出循环次数
            print("比较第{}次".format(j))         # 输出交换次数
            print(list) #输出列表
            if list[j] > list[j+1]:             # 如果左边大于右边
                list[j],list[j+1] = list[j+1],list[j]　# 左右交换

                print(list)

    # 返回排序的list
    return list　



#实例化一个列表，并输出排序序列
a = [5,10,8,1,4]
print(bubble_sort(a))