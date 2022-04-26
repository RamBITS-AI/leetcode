from enum import IntEnum

class Roman(IntEnum):
    I = 1,
    V = 5,
    X = 10,
    L = 50,
    C = 100,
    D = 500,
    M = 1000

    @staticmethod
    def getValue(s: str) -> int:
        return int(Roman[s.upper()])

class Solution:

    def __init__(self):
        self.prevSubtractionDigit = ""
        self.prevDigit = ""
        self.totalValue = 0
    
    def romanToInt(self, s: str) -> int:  #1895 | 1994
        for r in s:
            if r == Roman.I.name or r == Roman.X.name or r == Roman.C.name:
                if self.prevSubtractionDigit == "":
                    if self.prevDigit == "":
                        self.prevSubtractionDigit = r
                        # print("Mark#1", self.totalValue, r)
                    elif self.prevDigit == r:
                        self.prevDigit = ""
                        self.totalValue += Roman.getValue(r)         
                        # print("Mark#2", self.totalValue, r)
                    else:
                        self.totalValue += Roman.getValue(r)
                        self.prevDigit = ""
                        # print("Mark#2.5", self.totalValue, r)
                elif self.prevSubtractionDigit == r:
                    self.totalValue += Roman.getValue(r) + Roman.getValue(self.prevSubtractionDigit)
                    if r == self.prevSubtractionDigit:
                        self.prevDigit = r
                    self.prevSubtractionDigit = ""
                    self.prevDigit = ""
                    # print("Mark#3", self.totalValue, r)
                elif self.prevDigit == r:
                    self.prevSubtractionDigit = ""
                    self.prevDigit = ""
                    self.totalValue += Roman.getValue(r)
                    # print("Mark#4", self.totalValue, r)
                elif self.prevSubtractionDigit != "":
                    r_val = Roman.getValue(r)
                    prev_val = Roman.getValue(self.prevSubtractionDigit)
                    if prev_val > r_val:
                        self.totalValue += prev_val
                        self.prevSubtractionDigit = r
                    else:
                        self.totalValue += r_val - prev_val
                        self.prevSubtractionDigit = ""
                    # print("Mark#5", self.totalValue, r)
                else:
                    self.prevSubtractionDigit = ""
                    self.prevDigit = ""
                    # print("Mark#5.5", self.totalValue, r)
            elif self.prevSubtractionDigit == "":
                self.totalValue += Roman.getValue(r)
                self.prevDigit = ""
                # print("Mark#6", self.totalValue, r)
            else:
                r_val = Roman.getValue(r)
                prev_val = Roman.getValue(self.prevSubtractionDigit)
                if prev_val > r_val:
                    self.totalValue += Roman.getValue(self.prevSubtractionDigit) + Roman.getValue(r)
                else:
                    self.totalValue += Roman.getValue(r) - Roman.getValue(self.prevSubtractionDigit)
                self.prevSubtractionDigit = ""
                self.prevDigit = ""
                # print("Mark#7", self.totalValue, r)
        if self.prevSubtractionDigit != "":
            self.totalValue += Roman.getValue(self.prevSubtractionDigit)
        if self.prevDigit != "":
            self.totalValue += Roman.getValue(self.prevDigit)
        # print("Mark#8", self.totalValue, r)
        return self.totalValue
