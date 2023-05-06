def num_countd(self):
    self.countd = 0
    self.numd = 0
def countd(self, x = 4):
    if x == 4:
        if self.countd > 60:
            self.countd = 0
        self.countd += 1
    elif x == 11:
        if self.countd > 140:
            self.countd = 0
        self.countd += 1
def counterd(self, x = 4):
    if x == 4:
        if self.countd == 1:
            self.numd = 0
        elif self.countd == 20:
            self.numd = 1
        elif self.countd == 40:
            self.numd = 2
        elif self.countd == 60:
            self.numd = 3
    elif x == 11:
        if self.countd == 1:
            self.numd = 0
        elif self.countd == 10:
            self.numd = 1
        elif self.countd == 20:
            self.numd = 2
        elif self.countd == 30:
            self.numd = 3
        elif self.countd == 40:
            self.numd = 4
        elif self.countd == 50:
            self.numd = 5
        elif self.countd == 60:
            self.numd = 6
        elif self.countd == 70:
            self.numd = 7
        elif self.countd == 80:
            self.numd = 8
        elif self.countd == 90:
            self.numd = 9
        elif self.countd == 100:
            self.numd = 10
        elif self.countd == 110:
            self.numd = 11
        elif self.countd == 115:
            self.numd = 12
        elif self.countd == 120:
            self.numd = 13
        elif self.countd == 125:
            self.numd = 14
        elif self.countd == 130:
            self.numd = 15

