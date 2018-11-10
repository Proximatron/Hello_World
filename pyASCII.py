import os
import msvcrt
import time

ScreenWidth = 10
ScreenHeight = 10


class Image():
    def __init__(self, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10):
        self.l1 = line1
        self.l2 = line2
        self.l3 = line3
        self.l4 = line4
        self.l5 = line5
        self.l6 = line6
        self.l7 = line7
        self.l8 = line8
        self.l9 = line9
        self.l10 = line10
        self.location = [5,4]

    def return_all_lines(self):
        self.all_lines = [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9, self.l10]
        return self.all_lines

    def draw(self, hello):
        for elements in hello:
            print(elements)

    def add_character(self):
        list6 = list(self.l6)
        list6[self.location[0]] = "@"
        self.l6 = "".join(list6)

    def character_loc(self, all_lines):
        self.all_lines = all_lines
        if "@" in list(self.all_lines[0]):
            locy = 0
            line = list(self.all_lines[0])
        elif "@" in list(self.all_lines[1]):
            locy = 1
            line = list(self.all_lines[1])
        elif "@" in list(self.all_lines[2]):
            locy = 2
            line = list(self.all_lines[2])
        elif "@" in list(self.all_lines[3]):
            locy = 3
            line = list(self.all_lines[3])
        elif "@" in list(self.all_lines[4]):
            locy = 4
            line = list(self.all_lines[4])
        elif "@" in list(self.all_lines[5]):
            locy = 5
            line = list(self.all_lines[5])
        elif "@" in list(self.all_lines[6]):
            locy = 6
            line = list(self.all_lines[6])
        elif "@" in list(self.all_lines[7]):
            locy = 7
            line = list(self.all_lines[7])
        elif "@" in list(self.all_lines[8]):
            locy = 8
            line = list(self.all_lines[8])
        elif "@" in list(self.all_lines[9]):
            locy = 9
            line = list(self.all_lines[9])
        else:
            print("There is no @ on screen")
        if "@" in line:
            locx = line.index("@")
        self.location = [locx, locy]
        print(self.location)

    def character_move(self, keeper, cur_location):
        movement = msvcrt.getch()
        location = cur_location
        st_location = True
        try:
            if movement == b'w':
                hello = list(self.all_lines[self.location[1] - 1])
                keepsake = hello[self.location[0]]
                if keepsake == "#":
                    keepsake/2
                hello = list(self.all_lines[self.location[1]-1])
                hello[self.location[0]] = "@"
                self.all_lines[self.location[1]-1] = "".join(hello)
                hello2 = list(self.all_lines[self.location[1]])
                hello2[self.location[0]] = keeper
                self.all_lines[self.location[1]] = "".join(hello2)
            if movement == b'd':
                hello = list(self.all_lines[self.location[1]])
                keepsake = hello[self.location[0]+1]
                if keepsake == "#":
                    keepsake/2
                elif keepsake == "/":
                    location = Block2
                    #time.sleep(2)
                    print("Moving Area")
                    time.sleep(2)
                    st_location = False
                hello = list(self.all_lines[self.location[1]])
                hello[self.location[0]+1] = "@"
                self.all_lines[self.location[1]] = "".join(hello)
                hello2 = list(self.all_lines[self.location[1]])
                hello2[self.location[0]] = keeper
                self.all_lines[self.location[1]] = "".join(hello2)
            if movement == b's':
                hello = list(self.all_lines[self.location[1]+1])
                keepsake = hello[self.location[0]]
                if keepsake == "#":
                    keepsake/2
                hello = list(self.all_lines[self.location[1]+1])
                hello[self.location[0]] = "@"
                self.all_lines[self.location[1]+1] = "".join(hello)
                hello2 = list(self.all_lines[self.location[1]])
                hello2[self.location[0]] = keeper
                self.all_lines[self.location[1]] = "".join(hello2)
            if movement == b'a':
                hello = list(self.all_lines[self.location[1]])
                keepsake = hello[self.location[0]-1]
                if keepsake == "#":
                    keepsake/2
                hello = list(self.all_lines[self.location[1]])
                hello[self.location[0]-1] = "@"
                self.all_lines[self.location[1]] = "".join(hello)
                hello2 = list(self.all_lines[self.location[1]])
                hello2[self.location[0]] = keeper
                self.all_lines[self.location[1]] = "".join(hello2)
        except:
            keepsake = keeper
        return self.all_lines, keepsake, location, st_location

Block = Image("#################################",
              "#                       #       #",
              "#                       #       #",
              "#                       #       #",
              "#                       #       #",
              "#                               #",
              "#                       #       #",
              "#                       #########",
              "#                               /",
              "#################################")

Block2 = Image("############   ##################",
               "# /^\    ,,..,...,.     #       #",
               "#//^           ,.,.     #       #",
               "#//^             ,.,    #       #",
               "#//^              ,..,. #       #",
               "#//^              ,.,.          #",
               "#//^             ..,.,. #       #",
               "#/   \              ,.,.#########",
               "#|   |,..,,.,..,...,.,,.,,..,.,.,",
               "#################################")

location = Block
while True:
    ral = location.return_all_lines()
    location.draw(ral)
    location.add_character()
    ral = location.return_all_lines()
    os.system('cls')
    location.draw(ral)
    location.character_loc(ral)
    keeper = " "
    ral = location.character_move(keeper, location)
    st_location = True
    while st_location == True:
        location = ral[2]
        st_location = ral[3]
        os.system('cls')
        location.draw(ral[0])
        location.character_loc(ral[0])
        ral = location.character_move(ral[1], location)

