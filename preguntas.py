
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

class Preguntas:    
        
    def __init__(self,n):
        self.s = 0
        if n == 1:
            for i in range(8):
                ops = random.randint(1,2)
                num1 = random.randint(0,50)
                num2 = random.randint(0,50)

                if ops == 1:
                    self.q = (input("What is {} + {}? ".format(num1,num2)))
                    self.ans = num1 + num2
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
                else:
                    self.q = (input("What is {} - {}? ".format(num1,num2)))
                    self.ans = num1 - num2
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
            
        elif n == 2:
            for i in range(10):
                ops = random.randint(1,3)
                num1 = random.randint(0,50)
                num2 = random.randint(0,50)

                if ops == 1:
                    self.q = (input("What is {} + {}? ".format(num1,num2)))
                    self.ans = num1 + num2
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
                elif ops == 2:
                    self.q = (input("What is {} - {}? ".format(num1,num2)))
                    self.ans = num1 - num2
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
                else:
                    self.q = (input("What is {} * {}? ".format(num1,num2)))
                    self.ans = num1 * num2
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
        else:
            for i in range(12):
                ops = random.randint(1,4)
                num1 = random.randint(0,50)
                num2 = random.randint(0,50)
                num3 = random.randint(1,15)
                num4 = random.randint(1,15)*2

                if ops == 1:
                    self.q = (input("What is {} + {}? ".format(num1,num2)))
                    self.ans = num1 + num2
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
                    print(self.ans)
                elif ops == 2:
                    self.q = (input("What is {} - {}? ".format(num1,num2)))
                    self.ans = num1 - num2
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
                    print(self.ans)
                elif ops == 3:
                    self.q = (input("What is {} * {}? ".format(num3,num4)))
                    self.ans = num3 * num4
                    if check(self.q) == True:
                        if self.ans == int(self.q):
                            self.s +=1
                    print(self.ans)
                else:
                    self.q = (input("What is {}/{}? ".format(num3,num4)))
                    self.ans = num3/num4
                    ans = round(self.ans,2)
                    if check(self.q) == True:
                        if ans == float(self.q):
                            self.s +=1
                    print(ans)
        
                
    
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
    

     

