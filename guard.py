from tkinter import *
from random import *

#global constants
easy_difficulty = 0
medium_difficulty = 1
hard_difficulty = 2


class Guard:
    def __init__(self, x, y, x_dir, y_dir, moving_vert):
        self.x = x
        self.y = y
        self.x_speed = 10
        self.y_speed = 10
        self.detect_range = 120
        self.size = 25
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.moving_vert = moving_vert
        self.drawing = 0
        self.flashlight = 0

    def update_pos(self):
        if self.moving_vert:
            self.y += self.y_speed * self.y_dir
        else:
            self.x += self.x_speed * self.x_dir

    def update_movement(self, difficulty, intersections, i):
        if difficulty == easy_difficulty:
            for x in range(len(intersections)):
                if intersections[x][0][0] <= self.x <= intersections[x][1][0] and\
                   intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x in [1,7,11]:
                        if self.moving_vert and self.y_dir == 1:
                            self.moving_vert = False
                            self.x_dir = -1

                        elif self.moving_vert == False and self.x_dir == 1:
                            self.moving_vert = True
                            self.y_dir = -1

                    elif x in [0,13]:
                        if self.moving_vert == False and self.x_dir == -1:
                            self.x_dir = 1

                    elif x in [2,8,12]:                        
                        if self.moving_vert and self.y_dir == -1:
                            self.moving_vert = False
                            self.x_dir = -1

                        elif self.moving_vert == False and self.x_dir == 1:
                            self.moving_vert = True
                            self.y_dir = 1

                    elif x in [3,6,10]:
                        if self.moving_vert == False and self.x_dir == -1:
                            self.moving_vert = True
                            self.y_dir = 1

                        elif self.moving_vert and self.y_dir == -1:
                            self.moving_vert = False
                            self.x_dir = 1

                    elif x == 4:
                        if self.moving_vert and self.y_dir == 1:
                            self.y_dir = -1

                    elif x == 5:
                        if self.moving_vert and self.y_dir == 1:
                            self.y_dir = -1

                        elif self.moving_vert == False and self.x_dir == -1:
                            self.moving_vert = True
                            self.y_dir = -1 

                    elif x == 9:
                        if self.moving_vert == False and self.x_dir == -1:
                            self.moving_vert = True
                            self.y_dir = -1

                        elif self.moving_vert and self.y_dir == 1:
                            self.moving_vert = False
                            self.x_dir = 1

        elif difficulty == medium_difficulty:
            for x in range(len(intersections)):
                if intersections[x][0][0] <= self.x <= intersections[x][1][0] and \
                   intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x == 0:
                        if self.moving_vert == False and self.x_dir == -1:
                            self.moving_vert = True
                            self.y_dir = 1

                        elif self.moving_vert and self.y_dir == -1:
                            self.moving_vert = False
                            self.x_dir = 1

                    elif x == 1:
                        if (i == 1 and self.moving_vert and self.y_dir == 1) \
                           or (i == 0 and self.moving_vert == False and \
                               self.x_dir == -1):

                            self.moving_vert = False
                            self.x_dir = 1
                            

                        elif i == 1 and self.moving_vert == False \
                             and self.x_dir == -1:

                            self.moving_vert = True
                            self.y_dir = -1

                    elif x == 2:
                        if i == 1 and self.moving_vert == False and \
                           self.x_dir == 1:

                            self.x_dir = -1

                    elif x == 3:
                        if self.moving_vert and self.y_dir == 1:
                            self.moving_vert = False
                            self.x_dir = -1

                        elif self.moving_vert == False and self.x_dir == 1:
                            self.moving_vert = True
                            self.y_dir = -1

                    elif x == 4:
                        if self.moving_vert == False and self.x_dir == -1:
                            self.moving_vert = True
                            self.y_dir = -1

                        elif self.moving_vert and self.y_dir == 1:
                            self.moving_vert = False
                            self.x_dir = 1

                    elif x == 5:
                        if i == 0:
                            if self.moving_vert and self.y_dir == -1:
                                self.moving_vert = False
                                self.x_dir = -1

                            elif self.moving_vert == False and self.x_dir == 1:
                                self.moving_vert = True
                                self.y_dir = 1

                    elif x == 6:
                        if self.moving_vert and self.y_dir == -1:
                            self.y_dir = 1

                    elif x == 7:
                        if self.moving_vert == False and self.x_dir == 1:
                            self.x_dir = -1                  

        elif difficulty == hard_difficulty:       
            for x in range(len(intersections)):
                if intersections[x][0][0] <= self.x <= intersections[x][1][0] and \
                   intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x == 0 or x == 14:
                        if choice([1,2]) == 1:
                            self.x_dir = -1
                            self.moving_vert = False

                        else:
                            self.y_dir = -1
                            self.moving_vert = True

                    elif x == 1 or x == 7 or x == 13:
                        if choice([1,2]) == 1:
                            self.y_dir = -1
                            self.moving_vert = True

                        else:
                            self.x_dir = 1
                            self.moving_vert = False

                    elif x == 2 or x == 11:
                        if choice([1,2]) == 1:
                            self.y_dir = 1
                            self.moving_vert = True
                            
                        else:
                            self.x_dir = 1
                            self.moving_vert = False
                            
                    elif x == 3:
                        dieRoll = choice([1,2,3])
                        if dieRoll == 1:
                            self.x_dir = -1
                            self.moving_vert = False

                        elif dieRoll == 2:
                            self.y_dir = -1
                            self.moving_vert = True

                        else:
                            self.y_dir = 1
                            self.moving_vert = True

                    elif x == 4 or x == 8:
                        dieRoll = choice([1,2,3])
                        if dieRoll == 1:
                            self.x_dir = -1
                            self.moving_vert = False

                        elif dieRoll == 2:
                            self.x_dir = 1
                            self.moving_vert = False

                        else:
                            self.y_dir = 1
                            self.moving_vert = True

                    elif x == 5 or x == 6:
                        dieRoll = choice([1,2,3])
                        if dieRoll == 1:
                            self.x_dir = -1
                            self.moving_vert = False

                        elif dieRoll == 2:
                            self.x_dir = 1
                            self.moving_vert = False

                        else:
                            self.y_dir = -1
                            self.moving_vert = True

                    elif x == 9:
                        self.x_dir = -1

                    elif x == 10 or x == 15:
                        self.y_dir = 1

                    elif x == 12:
                        if choice([1,2]) == 1:
                            self.y_dir = 1
                            self.moving_vert = True

                        else:
                            self.x_dir = -1
                            self.moving_vert = False
                            
                    if self.moving_vert:
                        self.x = (intersections[x][0][0] + intersections[x][1][0]) / 2

                    else:
                        self.y = (intersections[x][0][1] + intersections[x][1][1]) / 2

    def update_detect_range(self, difficulty, intersections):
        if difficulty == easy_difficulty:
            for x in range(len(intersections)):
                if self.moving_vert and self.y_dir == -1 and \
                   0 <= self.y - (intersections[x][0][1] - 40) <= 120 and \
                   intersections[x][0][0] <= self.x <= intersections[x][1][0]:

                    if x in [2,3]:
                        self.detect_range = self.y - (intersections[x][0][1] - 53)
                        break

                    elif x in [8,10]:
                        self.detect_range = self.y - (intersections[x][0][1] - 40)
                        break

                    elif x == 6:
                        self.detect_range = self.y - (intersections[x][0][1] - 35)
                        break

                    elif x == 12:
                        self.detect_range = self.y - (intersections[x][0][1] - 50)
                        break

                    else:
                        self.detect_range = 120
                elif self.moving_vert and self.y_dir == 1 and \
                     0 <= intersections[x][0][1] + 47 - self.y <= 120 and \
                     intersections[x][0][0] <= self.x <= intersections[x][1][0]:

                    if x == 1:
                        self.detect_range = intersections[x][0][1] + 44 - self.y
                        break

                    if x in [9,11]:
                        self.detect_range = intersections[x][0][1] + 47 - self.y
                        break

                    elif x == 5:
                        self.detect_range = intersections[x][0][1] + 42 - self.y
                        break


                    elif x in [4,7]:
                        self.detect_range = intersections[x][0][1] + 53 - self.y
                        break

                    else:
                        self.detect_range = 120
                
                elif self.moving_vert == False and self.x_dir == 1 and \
                     0 <= intersections[x][0][0] + 50 - self.x <= 120 and \
                     intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x in [1,2]:
                        self.detect_range = intersections[x][0][0] + 52 - self.x
                        break

                    elif x in [8,11]:
                        self.detect_range = intersections[x][0][0] + 65 - self.x
                        break

                    else:
                        self.detect_range = 120

                elif self.moving_vert == False and self.x_dir == -1 and \
                     0 <= self.x - (intersections[x][1][0] - 44)  <= 120 and \
                     intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x in [5,6,9,10,13]:
                        self.detect_range = self.x - (intersections[x][1][0] - 58) 
                        break

                    elif x == 3:
                        self.detect_range = self.x - (intersections[x][1][0] - 44) 
                        break 
                        
                    else:
                        self.detect_range = 120

        elif difficulty == medium_difficulty:
            for x in range(len(intersections)):
                if self.moving_vert and self.y_dir == -1 and \
                   0 <= self.y - (intersections[x][0][1] - 60) <= 120 and \
                   intersections[x][0][0] <= self.x <= intersections[x][1][0]:

                    if x in [0,6]:
                        self.detect_range = self.y - (intersections[x][0][1] - 53)

                    elif x == 5:
                        self.detect_range = self.y - (intersections[x][0][1] - 62)

                    else:
                        self.detect_range = 120

                elif self.moving_vert and self.y_dir == 1 and \
                     0 <=  intersections[x][0][1] + 43 - self.y <= 120 and \
                     intersections[x][0][0] <= self.x <= intersections[x][1][0]:

                    if x == 1:
                        self.detect_range = intersections[x][0][1] + 67 - self.y

                    elif x in [3,4]:
                        self.detect_range = intersections[x][0][1] + 43 - self.y

                    else:
                        self.detect_range = 120

                elif self.moving_vert == False and self.x_dir == -1 and \
                     0 <= self.x - (intersections[x][1][0] - 68)  <= 120 and \
                     intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x in [0,1]:
                        self.detect_range = self.x - (intersections[x][1][0] - 68)

                    else:
                        self.detect_range = 120

                elif self.moving_vert == False and self.x_dir == 1 and \
                     0 <= intersections[x][1][0] + 52 - self.x <= 120 and \
                     intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x == 3:
                        self.detect_range = intersections[x][1][0] + 52 - self.x

                    elif x == 7:
                        self.detect_range = intersections[x][1][0] + 100 - self.x

                    else:
                        self.detect_range = 120

        elif difficulty == hard_difficulty:
            for x in range(len(intersections)):
                if self.moving_vert and self.y_dir == 1 and \
                   0 <= intersections[x][0][1] + 45 - self.y <= self.detect_range\
                   and intersections[x][0][0] <= self.x <= intersections[x][1][0]:

                    if x == 7:
                        self.detect_range = intersections[x][0][1] + 62 - self.y
                        break

                    elif x in [0,1,6]:
                        self.detect_range = intersections[x][0][1] + 42 - self.y
                        break
                        
                    elif x in [5,13,14]:
                        self.detect_range = intersections[x][0][1] + 45 - self.y
                        break

                    else:
                        self.detect_range = 120
                        
                elif self.moving_vert and self.y_dir == -1 and \
                     0 <= self.y - (intersections[x][0][1] - 53) <= self.detect_range\
                     and intersections[x][0][0] <= self.x <= intersections[x][1][0]:

                    if x in [2,8,10]:
                        self.detect_range = self.y - (intersections[x][0][1]-53) 
                        break

                    elif x == 4:
                        self.detect_range = self.y - (intersections[x][0][1]-30)
                        break                        

                    elif x in [11,12,15]:
                        self.detect_range = self.y - (intersections[x][0][1]-68) 
                        break

                    else:
                        self.detect_range = 120

                elif self.moving_vert == False and self.x_dir == 1 and \
                     0 <= intersections[x][1][0] + 45 - self.x <= self.detect_range\
                     and intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x in [0,3]:
                        self.detect_range = intersections[x][1][0] + 53 - self.x
                        break

                    elif x == 12:
                        self.detect_range = intersections[x][1][0] + 27 - self.x
                        break

                    elif x == 14:
                        self.detect_range = intersections[x][1][0] + 52 - self.x
                        break

                    else:
                        self.detect_range = 120

                elif self.moving_vert == False and self.x_dir == -1 and \
                     0 <= self.x - (intersections[x][0][0] - 35) <= self.detect_range\
                     and intersections[x][0][1] <= self.y <= intersections[x][1][1]:

                    if x in [1,2]:
                        self.detect_range = self.x - (intersections[x][0][0] - 35)
                        break

                    elif x in [7,11]:
                        self.detect_range = self.x - (intersections[x][0][0] - 60)
                        break

                    elif x == 13:
                        self.detect_range = self.x - (intersections[x][0][0] - 43)
                        break

                    else:
                        self.detect_range = 120
     
                else: 
                    self.detect_range = 120

    # returns whether the game is still running as well
    # draws the flashlight sightlines for each guard, based on the
    #   detection range and direction the guard is moving
    # Note: runs the .caught() method if the player is within detection range
    def draw_flashlight(self, screen, player, guard_list):
        if self.moving_vert:
            self.flashlight = screen.create_polygon(
                self.x, self.y + self.size * self.y_dir,
                self.x + self.size,
                self.y + self.detect_range * self.y_dir,
                self.x - self.size,
                self.y + self.detect_range * self.y_dir,
                fill="yellow", outline="black"
                )

            if self.y_dir == -1 and \
               self.x-self.size <= player.x \
               <= self.x+self.size and \
               self.y - self.detect_range - player.height \
               <= player.y \
               <= self.y + self.size + player.height:
                
                return player.caught(guard_list)

            elif self.y_dir == 1 and \
                 self.x - self.size <= player.x <= self.x + self.size and \
                 self.y - self.size - player.height <= player.y \
                 <= self.y + self.detect_range + player.height:

                return player.caught(guard_list)
            else:
                return True

        else:                
            self.flashlight = screen.create_polygon(
                self.x + self.size * self.x_dir,
                self.y,
                self.x + self.detect_range * self.x_dir,
                self.y - self.size,
                self.x + self.detect_range * self.x_dir,
                self.y + self.size,
                fill="yellow", outline="black"
                )

            if self.x_dir == -1 and \
               self.y-self.size <= player.y \
               <= self.y + self.size and \
               self.x - self.detect_range - player.width \
               <= player.x <= \
               self.x + self.size + player.width:
                
                return player.caught(guard_list) 

            elif self.x_dir == 1 and \
                 self.y - self.size <= player.y \
                 <= self.y + self.size and \
                 self.x - self.size - player.width \
                 <= player.x <= \
                 self.x + self.detect_range + player.width:

                return player.caught(guard_list)
            else:
                return True
        
    # draws guards and flashlights and returns a new value for game_running
    def draw(self, difficulty, intersections, screen, player, paused, game_clock,
             guard_run_right, guard_run_left, guard_run_up, guard_run_down,
             guard_list):

        self.update_detect_range(difficulty, intersections)
        game_running = self.draw_flashlight(screen, player, guard_list)

        # if the game is no longer running, return False and don't run the rest
        #   of the function
        if not game_running:
            return False

        # pause guard animations 
        if paused:
            if self.moving_vert and self.y_dir == 1:
                self.drawing = screen.create_image(
                    self.x, self.y, image = guard_run_down[0]
                    )

            elif self.moving_vert and self.y_dir == -1:
                self.drawing = screen.create_image(
                    self.x, self.y, image = guard_run_up[0]
                    )

            elif self.moving_vert == False and self.x_dir == -1:
                self.drawing = screen.create_image(
                    self.x, self.y, image = guard_run_left[0]
                    )

            elif self.moving_vert == False and self.x_dir == 1:
                self.drawing = screen.create_image(
                    self.x, self.y, image = guard_run_right[0]
                    )

            return True

        else:
            if self.moving_vert and self.y_dir == 1:
                f = game_clock.frame_count % 9
                self.drawing = screen.create_image(
                    self.x, self.y, image = guard_run_down[f]
                    )
                
            elif self.moving_vert == False and self.x_dir == 1:
                f = game_clock.frame_count % 9
                self.drawing = screen.create_image(
                    self.x, self.y, image = guard_run_right[f]
                    )

            elif self.moving_vert and self.y_dir == -1:
                f = game_clock.frame_count % 9
                self.drawing = screen.create_image(
                    self.x, self.y, image=guard_run_up[f]
                    )

            elif self.moving_vert == False and self.x_dir == -1:
                f = game_clock.frame_count % 9
                self.drawing = screen.create_image(
                    self.x, self.y, image = guard_run_left[f]
                    )

            return True
