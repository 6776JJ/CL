
#-*-coding:utf-8-*-
#作者:CL
#创建日期:31,12,2021
#更新日期:1,1,2021
#目的: 实现2021
import sys
import os
import random
import itertools
#self.grid=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def up(gird):
    L1,L2,L3,L4=[],[],[],[]
    for k in range(0,4):
        L1.append(gird[k][0]),L2.append(gird[k][1]),L3.append(gird[k][2]),L4.append(gird[k][3])
    def zhuan(a):
        def X(b):
            for i in range(3):
                if b[i] == b[i + 1]:
                    b[i] *= 2
                    b[i + 1] = 0
            for j in range(3):
                if b[j] == 0:
                    b[j], b[j + 1] = b[j + 1], 0
            return b
        while 0 in a:
            a.remove(0)

        return X((a+[0,0,0,0])[:4])

    L1,L2,L3,L4=zhuan(L1),zhuan(L2),zhuan(L3),zhuan(L4)
    gird = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for n in range(4):
        gird[n][0]=L1[n]
        gird[n][1]=L2[n]
        gird[n][2]=L3[n]
        gird[n][3]=L4[n]
    return gird

def down(gird):
    L1, L2, L3, L4 = [], [], [], []
    for k in range(0,4):
        L1.append(gird[k][0]),L2.append(gird[k][1]),L3.append(gird[k][2]),L4.append(gird[k][3])
    def zhuan1(a):
        def X(b):
            for i in range(-1, -4, -1):
                if b[i] == b[i - 1]:
                    b[i] *= 2
                    b[i - 1] = 0
            for j in range(-1, -4, -1):
                if b[j] == 0:
                    b[j], b[j - 1] = b[j - 1], 0
            return b
        while 0 in a:
            a.remove(0)
        return X(([0,0,0,0]+a)[-4:])

    L1,L2,L3,L4=zhuan1(L1),zhuan1(L2),zhuan1(L3),zhuan1(L4)

    gird = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for n in range(4):
        gird[n][0]=L1[n]
        gird[n][1]=L2[n]
        gird[n][2]=L3[n]
        gird[n][3]=L4[n]
    return gird

def left(gird):
    L1,L2,L3,L4=gird[0],gird[1],gird[2],gird[3]
    def zhuan(a):
        def X(b):
            for i in range(3):
                if b[i] == b[i + 1]:
                    b[i] *= 2
                    b[i + 1] = 0
            for j in range(3):
                if b[j] == 0:
                    b[j], b[j + 1] = b[j + 1], 0
            return b
        while 0 in a:
            a.remove(0)

        return X((a+[0,0,0,0])[:4])

    L1,L2,L3,L4=zhuan(L1),zhuan(L2),zhuan(L3),zhuan(L4)
    gird = []
    gird.append(L1)
    gird.append(L2)
    gird.append(L3)
    gird.append(L4)

    return gird

def right(gird):
    L1, L2, L3, L4 = gird[0], gird[1], gird[2], gird[3]
    def zhuan1(a):
        def X(b):
            for i in range(-1, -4, -1):
                if b[i] == b[i - 1]:
                    b[i] *= 2
                    b[i - 1] = 0
            for j in range(-1, -4, -1):
                if b[j] == 0:
                    b[j], b[j - 1] = b[j - 1], 0
            return b
        while 0 in a:
            a.remove(0)
        return X(([0,0,0,0]+a)[-4:])

    L1,L2,L3,L4=zhuan1(L1),zhuan1(L2),zhuan1(L3),zhuan1(L4)

    gird = []
    gird.append(L1)
    gird.append(L2)
    gird.append(L3)
    gird.append(L4)

    return gird


class Game:
    grid=[]
    controls=["w","s","a","d"]
    def rnd_field(self):
        number=random.choice([4,2,2,4,4,2,2,4,2,4,2,4])
        all_xy=[]
        for x,y in itertools.product([0,1,2,3],[0,1,2,3]):
            all_xy.append([x,y])
        init_xy=random.choice(all_xy)

        while self.grid[init_xy[0]][init_xy[1]]!=0:
            init_xy=random.choice(all_xy)
        self.grid[init_xy[0]][init_xy[1]]=number

    def print_screen(self):
        #os.system("clear")
        print("-"*24)
        for row in self.grid:
            for col in row:
                #print("|{}|".format("|".join(str(col).center(4))))
                print("|{}|".format(str(col or " ").center(4)),end="")
            print("")
            print("-" * 24)



    def logic(self,control):
        grid = {'w': up, 'a': left, 's': down, 'd': right}[control]([[c for c in r] for r in self.grid])
        if grid!=self.grid:
            del self.grid[:]
            self.grid.extend(grid)
            if [n for n in itertools.chain(*grid) if n >= 2048]:

                return 1, "You Win!"
            self.rnd_field()
        else:
            cm=[]
            cm.append(down([[c for c in r] for r in self.grid]))
            cm.append(up([[c for c in r] for r in self.grid]))
            cm.append(left([[c for c in r] for r in self.grid]))
            cm.append(right([[c for c in r] for r in self.grid]))
            if cm[0]==cm[1]==cm[2]==cm[3]:
                return 1,"You Lost"
        return 0,"weiter"


    def main_loop(self):
        #self.grid=[[2, 0, 0, 2], [2, 2, 2, 2],[2, 0, 2, 2],[2, 2, 2, 2]]
        #self.grid=[[1,2,3,4],[5,0,7,8],[0,11,12,13],[14,15,16,17]]
        self.grid=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.rnd_field()
        self.rnd_field()
        while 1:
            self.print_screen()#刷新屏幕
            control=input("w,s,a,d:") # choice Richtung
            if control in self.controls: #if choice Richtung in wasd
                status,info=self.logic(control)  #go logic (choice Richtung)
                if status!=0:#if status !=0  游戏不能进行下去
                    print(info)#输赢
                    if input("y/n").lower()=="y":
                        break#weiter
                    else:
                        sys.exit(0)#end
        self.main_loop()

if __name__=="__main__":
    Game().main_loop()