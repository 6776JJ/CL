#-*-coding:utf-8-*-
#作者:CL
#创建日期:31,12,2021
#更新日期:1,15,2022
#目的: 实现2021

import sys
import random
import itertools
import msvcrt

def del_0(b):
    while 0 in b:
        b.remove(0)
    return b
def left_add(b):
    b = del_0(b)
    length = len(b)
    if length < 2:
        return b
    if length >= 2:
        for i in range(0, length - 1):
            if b[i] == b[i + 1]:
                b[i] = b[i] * 2
                del b[i + 1]
                b.append(0)
        return b
def right_add( b):
    b = del_0(b)
    b.reverse()
    length = len(b)
    if length < 2:
        return b
    if length >= 2:
        for i in range(0, length - 1):
            if b[i] == b[i + 1]:
                b[i] = b[i] * 2
                del b[i + 1]
                b.append(0)
        b.reverse()
        return b
def up(gird):
    for i in zip(*gird):
        gird.append(list(i))
    for j in range(4, 8):
        gird[j] = (left_add(gird[j]) + [0, 0, 0, 0])[:4]
    for k in zip(gird[4], gird[5], gird[6],gird[7]):
        gird.append(list(k))
    gird = gird[8:]
    return gird
def down(gird):
    for i in zip(*gird):
        gird.append(list(i))
    gird = gird[4:]
    for j in range(4):
        gird[j] = ([0, 0, 0, 0] + right_add(gird[j]))[-4:]
    for k in zip(gird[0], gird[1], gird[2], gird[3]):
        gird.append(list(k))
    gird = gird[4:]
    return gird
def left(gird):
    for i in range(4):
        gird[i] = (left_add(gird[i]) + [0, 0, 0, 0])[:4]
    return gird
def right(gird):
    for i in range(4):
        gird[i] = ([0, 0, 0, 0] + right_add(gird[i]))[-4:]
    return gird


class Game:
    grid=[]
    controls=[b"w",b"s",b"a",b"d"]
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
        a = "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+"
        print("\n" + a)
        for i in self.grid:
            print("|" + (("|").join([("{}".format(str(j or " ").center(5))) for j in i])) + "|", ("\n" + a))
    def logic(self,control):
        grid = {b'w': up, b'a': left, b's': down, b'd': right}[control]([[c for c in r] for r in self.grid])
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
        self.grid=[[0, 0, 2, 0], [4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.rnd_field()
        self.rnd_field()

        while 1:
            self.print_screen()#刷新屏幕
            a = msvcrt.getch()
            if a in self.controls:
                status,info=self.logic(a)  #go logic (choice Richtung)
                if status!=0:#if status !=0  游戏不能进行下去
                    print(info)#输赢
                    if input("y/n").lower()=="y":
                        break#weiter
                    else:
                        sys.exit(0)#end
        self.main_loop()


if __name__=="__main__":
    Game().main_loop()
