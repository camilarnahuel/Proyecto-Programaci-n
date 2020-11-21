
import random

def check(x):
    if x.isdigit() != True:
        if ("-" in x) or ("." in x):
            return True
        else:
            print("Hey Pal, not a valid answer.")
            return False
    else:
        return True

class Operations:
    def add(self):
        num1 = random.randint(0,50)
        num2 = random.randint(0,50)
        self.q = (input("What is {} + {}? ".format(num1,num2)))
        self.ans = num1 + num2

    def res(self):
        num1 = random.randint(0,50)
        num2 = random.randint(0,50)
        self.q = (input("What is {} - {}? ".format(num1,num2)))
        self.ans = num1 - num2

    def mul(self):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        self.q = (input("What is {} * {}? ".format(num1,num2)))
        self.ans = num1 * num2

    def div(self):
        num1 = random.randint(1,15)
        num2 = random.randint(1,15)*2
        self.q = (input("What is {}/{}? ".format(num1,num2)))
        self.ans = num1/num2

    def score(self):
        if check(self.q) == True:
            if self.ans == int(self.q):
                self.s +=1


class Preguntas(Operations):
    def __init__(self,n):
        self.s = 0
        if n == 1:
            for i in range(8):
                ops = random.randint(1,2)

                if ops == 1:
                    Operations.add(self)
                    Operations.score(self)
                else:
                    Operations.res(self)
                    Operations.score(self)

        elif n == 2:
            for i in range(10):
                ops = random.randint(1,3)

                if ops == 1:
                    Operations.add(self)
                    Operations.score(self)
                elif ops == 2:
                    Operations.res(self)
                    Operations.score(self)
                else:
                    Operations.mul(self)
                    Operations.score(self)
        else:
            for i in range(12):
                ops = random.randint(1,4)

                if ops == 1:
                    Operations.add(self)
                    Operations.score(self)
                elif ops == 2:
                    Operations.res(self)
                    Operations.score(self)
                elif ops == 3:
                    Operations.mul(self)
                    Operations.score(self)
                else:
                    Operations.div(self)
                    ans = round(self.ans,2)
                    if check(self.q) == True:
                        if ans == float(self.q):
                            self.s +=1



    def Preguntas_nivel(self,n):
        if n == 1:
            print("Your score is {0}/8".format(self.s))
            if self.s >= 5:
                print("Oh! You pass the level 1 :)")
                return True
            else:
                print("Game Over")
                return False

        if n == 2:
            print("Your score is {0}/10".format(self.s))
            if self.s >= 6:
                print("Oh! You pass the level 2 :)")
                return True
            else:
                print("Game Over")
                return False

        if n == 3:
            print("Your score is {0}/12".format(self.s))
            if self.s >= 7:
                print("You are a winner!!!")
                return True
            else:
                print("Game Over")
                return False
