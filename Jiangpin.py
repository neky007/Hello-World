'''
题目：
ABC三个箱子，其中一个箱子有奖品。让你任选一个箱子，然后主持人会帮你去掉一个错误答案，
现在你可以改变你的选择，或者坚持你的选择。
问题是：
你改变选择，获奖的机率大？还是坚持原来的选择，获奖的几率大呢？
'''
import  random

if __name__ == '__main__':
    Goal=0

    for i in range(1000000):
        A=False
        B=False
        C=False

        # 放入奖品
        Money=random.choice("A""B""C")
        boxes=["A","B","C"]
        print("Money is ",Money)

        #我的选择
        Mynumber=random.choice("A""B""C")
        print("Mynumber is ",Mynumber)

        #去除一个错误答案
        boxes.remove(Money)
        try:
            boxes.remove(Mynumber)
        except ValueError:
            pass
        Wrongnumber=random.choice(boxes)
        print("Wrongnumber is ",Wrongnumber)

        #改变选择
        boxes = ["A", "B", "C"]
        boxes.remove(Wrongnumber)
        boxes.remove(Mynumber)
        Mynumber=random.choice(boxes)
        print("Mynumber changed as  ",Mynumber)

        #判断是否中奖
        if Mynumber == Money:
            print("你中奖了！")
            Goal+=1
        else:
            print("你没有中奖!")
    print(Goal/1000000)

