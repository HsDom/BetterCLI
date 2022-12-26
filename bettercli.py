import keyboard,os
from colorama import init
from time import sleep
init()

#Menu Class - Creates a menu 
class Menu:
    def __init__(self, title):
        self.title = title
        self.elements = []
        self.index = 0

    def add_button(self, button, function):
        self.elements.append([1,button, function])

    def add_slider(self, slider, min, max, defualt, increment):
        self.elements.append([2,slider, min, max, defualt, increment])

    def add_checkbox(self, checkbox, defualt):
        self.elements.append([3,checkbox, defualt])

    def return_slider(self, slider):
         for i in range(len(self.elements)):
            if self.elements[i][1] == slider:
                return self.elements[i][4]

    def return_checkbox(self, checkbox):
        for i in range(len(self.elements)):
            if self.elements[i][1] == checkbox:
                return self.elements[i][2]

        

    def show(self):
        #print menu title
        def render():
            print(self.title)

            #print menu items
            for i in range(len(self.elements)):
                if i == self.index:
                    #red background, white text
                    if self.elements[i][0] == 1:
                        print("\033[41m", self.elements[i][1] + "\033[0m")
                    elif self.elements[i][0] == 2:
                        print("\033[41m ", self.elements[i][1] + f"< {self.elements[i][4]} >\033[0m")
                    elif self.elements[i][0] == 3:
                        if self.elements[i][2] == True:
                            print("\033[41m +", self.elements[i][1] + "\033[0m")
                        else:
                            print("\033[41m -", self.elements[i][1] + f"\033[0m")
                else:
                    #white background, black text
                    if self.elements[i][0] == 1:
                        print(self.elements[i][1]) 
                    elif self.elements[i][0] == 2:
                        print(self.elements[i][1] + f"< {self.elements[i][4]} >")
                    elif self.elements[i][0] == 3:
                        if self.elements[i][2] == True:
                            print("+", self.elements[i][1])
                        else:
                            print("-", self.elements[i][1])

        #wait for a key press
        while True:
            os.system("cls")
            render()
            key = keyboard.read_key()

            #if up arrow key is pressed, go up
            if key == "up":
                if self.index > 0:
                    self.index -= 1
                    sleep(0.1)

            #if down arrow key is pressed, go down
            if key == "down":
                if self.index < len(self.elements) - 1:
                    self.index += 1
                    sleep(0.1)

            #check if the selected element is a slider
            if self.elements[self.index][0] == 2:
                #if left arrow key is pressed, go left
                if key == "left":
                    if self.elements[self.index][4] > self.elements[self.index][2]:
                        if (self.elements[self.index][4] - self.elements[self.index][5]) < self.elements[self.index][2]:
                            self.elements[self.index][4] = self.elements[self.index][2]
                        else:
                            #change the value of the variable Number
                            self.elements[self.index][4] -= self.elements[self.index][5]
                    sleep(0.1)

                #if right arrow key is pressed, go right
                if key == "right":
                    if self.elements[self.index][4] < self.elements[self.index][3]:
                        if (self.elements[self.index][4] + self.elements[self.index][5]) > self.elements[self.index][3]:
                            self.elements[self.index][4] = self.elements[self.index][3]
                        else:
                            #change the value of the variable Number
                            self.elements[self.index][4] += self.elements[self.index][5]
                    sleep(0.1)

            #if enter key is pressed, return the selected element
            if key == "enter":
                #run the function
                os.system("cls")
                #check if the selected element is a button
                if self.elements[self.index][0] == 1:
                    self.elements[self.index][2]()
                    break
                elif self.elements[self.index][0] == 3:
                    self.elements[self.index][2] = not self.elements[self.index][2]
                    sleep(0.1)