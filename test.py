from logging import raiseExceptions
import numpy as np
import itertools, random

class slot():
    def __init__(self):
        pass

    SLOT_ITEMS = [(":flag_us:",1),(":diamond_shape_with_a_dot_inside:",4),(":seven:",7),
                  (":peach:",13),(":apple:",21),(":cupcake:",21),(":eggplant:",33)]
    '''
    percentages{
    SLOT_ITEMS[0] = 1 %1    /
    SLOT_ITEMS[1] = 5 %4    /
    SLOT_ITEMS[2] = 13 %7   /
    SLOT_ITEMS[3] = 28 %13  / 
    SLOT_ITEMS[4] = 49 %21  /
    SLOT_ITEMS[5] = 70 %21  /
    SLOT_ITEMS[6] = 100 %33
    }
    '''
    slotpool = []

    def rec_slot(self,count,string):
        if count == 0:
            return 
        else:
            self.slotpool.append(string)
            self.rec_slot((count-1),string)

    def creatslot(self):
        self.slotpool = []
        for i in self.SLOT_ITEMS:
            self.rec_slot(i[1],i[0])
        random.shuffle(self.slotpool)

    def setSlotPos(self,num,vec1):
        vec2 = []
        vec2.append(vec1[num-1])
        vec2.append(vec1[num])
        try:
            vec2.append(vec1[num+1])
        except:
            vec2.append(vec1[0])
        return vec2
        

    def slotRoll(self):
        #self.SLOT_ONE = []
        #self.SLOT_THREE = []
        #self.SLOT_TWO = []
        self.SLOT_ONE_POS = []
        self.SLOT_TWO_POS = []
        self.SLOT_THREE_POS = []
        self.creatslot()

        random.shuffle(self.slotpool)
        slotnum = np.random.randint(100)
        self.SLOT_ONE_POS = self.setSlotPos(slotnum,self.slotpool)
        random.shuffle(self.slotpool)
        slotnum = np.random.randint(100)
        self.SLOT_TWO_POS = self.setSlotPos(slotnum,self.slotpool)
        random.shuffle(self.slotpool)
        slotnum = np.random.randint(100)
        self.SLOT_THREE_POS = self.setSlotPos(slotnum,self.slotpool)

    def getBonus(self):
        self.bonus = 0
        self.win = False
        #all three are same
        if self.SLOT_ONE_POS[1] == self.SLOT_TWO_POS[1] == self.SLOT_THREE_POS[1]:
            self.win = True
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[0][0]:
                self.bonus = 1000
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[1][0]:
                self.bonus = 50
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[2][0]:
                self.bonus = 10
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[3][0]:
                self.bonus = 5
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[4][0] or self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[5][0]:
                self.bonus = 3
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[6][0]:
                self.bonus = 1
        #if two are same
        elif self.SLOT_ONE_POS[1] == self.SLOT_TWO_POS[1]:
            self.win = True
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[0][0]:
                self.bonus = 500
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[1][0]:
                self.bonus = 25
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[2][0]:
                self.bonus = 5
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[3][0]:
                self.bonus = 2
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[4][0] or self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[5][0]:
                self.bonus = 1
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[6][0]:
                self.bonus = 0
        elif self.SLOT_TWO_POS[1] == self.SLOT_THREE_POS[1]:
            self.win = True
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[0][0]:
                self.bonus = 500
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[1][0]:
                self.bonus = 25
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[2][0]:
                self.bonus = 5
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[3][0]:
                self.bonus = 2
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[4][0] or self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[5][0]:
                self.bonus = 1
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[6][0]:
                self.bonus = 0
        #if none are same
        else:
            self.bonus = 0

    def slot(self):
        #credits = input("enter credits: ")
        self.bonus = 0
        self.slotRoll()
        for i in range(3):
            print(self.SLOT_ONE_POS[i] + self.SLOT_TWO_POS[i] + self.SLOT_THREE_POS[i])
        self.getBonus()
        print(f"you won {int(self.bonus)} credits")
        

    def playSlot(self):
        average = 0
        summ = 0
        countwin = 0
        for i in range(10):
            self.slot()
            if self.win == True:
                countwin +=1
            summ += int(self.bonus)

        average = summ/1000
        print(average)
        print(countwin)
     

thing = slot()
thing.playSlot()
