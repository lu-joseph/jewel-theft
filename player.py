from tkinter import *
from math import *
import clock

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.walk_speed = 7
        self.run_speed = 15
        self.width = 30
        self.height = 20
        self.got_jewel = False
        self.got_key = False
        self.got_caught = False
        self.won = False
        self.score = 0
        self.score_text = 0
        self.walk_right = []
        self.walk_left = []
        self.walk_up = []
        self.walk_down = []

    def set_starting_pos(self, difficulty):
        starting_pos = [(430, 200), (100, 250), (715, 250)]
        self.x = starting_pos[difficulty][0]
        self.y = starting_pos[difficulty][1]

    def import_images(self):
        self.idle_front = PhotoImage(file="sprites/player_idle_front.gif")
        walk_frames = 18
        run_frames = 9
        walk_sprites = [self.walk_right, self.walk_left, self.walk_up, self.walk_down]
        walk_files = ["sprites/player_walk_right.gif", "sprites/player_walk_left.gif",
                      "sprites/player_walk_up.gif", "sprites/player_walk_down.gif"]
        for i in range(len(walk_sprites)):
            for j in range(walk_frames):
                frame_text = "gif -index " + str(j)
                image = PhotoImage(file = walk_files[i],format = frame_text)
                walk_sprites[i].append(image)

        self.run_right = []
        self.run_left = []
        self.run_up = []
        self.run_down = []
        run_sprites = [self.run_right, self.run_left, self.run_up, self.run_down]
        run_files = ["sprites/player_run_right.gif", "sprites/player_run_left.gif",
                      "sprites/player_run_up.gif", "sprites/player_run_down.gif"]
        for i in range(len(run_sprites)):
            for j in range(run_frames):
                frame_text = "gif -index " + str(j)
                image = PhotoImage(file = run_files[i],format = frame_text)
                run_sprites[i].append(image)

    # returns a new value for game_running
    def caught(self, guards):
        self.got_caught = True
        self.x_speed = 0
        self.y_speed = 0
        for i in range(len(guards)):
            guards[i].x_speed = 0
            guards[i].y_speed = 0
        return False

    def draw(self, curr_keys, game_clock, screen):
        #different animations are used for the player based on direction and speed
        if "Left" in curr_keys and self.x_speed != 0:
            if "Shift_L" in curr_keys:
                i = game_clock.frame_count % 9
                return screen.create_image(
                    self.x, self.y, anchor=CENTER, image=self.run_left[i]
                    )
            else:
                i = game_clock.frame_count % 18
                return screen.create_image(
                    self.x, self.y, anchor=CENTER, image=self.walk_left[i]
                    )

        elif "Right" in curr_keys and self.x_speed != 0:
            if "Shift_L" in curr_keys:
                i = game_clock.frame_count % 9
                return screen.create_image(
                    self.x,self.y,anchor=CENTER,image=self.run_right[i]
                    )
            else:
                i = game_clock.frame_count % 18
                return screen.create_image(
                    self.x,self.y,anchor=CENTER,image=self.walk_right[i]
                    )

        elif "Down" in curr_keys and self.y_speed != 0:
            if "Shift_L" in curr_keys:
                i = game_clock.frame_count % 9
                return screen.create_image(
                    self.x, self.y, anchor=CENTER,image=self.run_down[i]
                    )
            else:
                i = game_clock.frame_count % 18
                return screen.create_image(
                    self.x, self.y, anchor=CENTER,image=self.walk_down[i]
                    )

        elif "Up" in curr_keys and self.y_speed != 0:
            if "Shift_L" in curr_keys:
                i = game_clock.frame_count % 9
                return screen.create_image(
                    self.x, self.y, anchor=CENTER,image=self.run_up[i]
                    )
            else:
                i = game_clock.frame_count % 18
                return screen.create_image(
                    self.x, self.y, anchor=CENTER,image=self.walk_up[i]
                    )

        else:
            return screen.create_image(
                self.x, self.y, anchor=CENTER,image=self.idle_front
                )

    def update_pos(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def update_speed(self, curr_keys):
        speed = 0

        if "Shift_L" in curr_keys:
            speed = self.run_speed

        else:
            speed = self.walk_speed

        if "Left" in curr_keys:
            if "Right" in curr_keys:
                self.x_speed = 0
                
            elif "Up" in curr_keys:
                self.x_speed = -1 * speed * sqrt(0.5)
                self.y_speed = -1 * speed * sqrt(0.5)

            elif "Down" in curr_keys:
                self.x_speed = -1 * speed * sqrt(0.5)
                self.y_speed = speed * sqrt(0.5)
                
            else:
                self.x_speed = -1 * speed
                self.y_speed = 0
            
        elif "Right" in curr_keys:
            if "Up" in curr_keys:
                self.x_speed = speed * sqrt(0.5)
                self.y_speed = -1 * speed * sqrt(0.5)

            elif "Down" in curr_keys:
                self.x_speed = speed * sqrt(0.5)
                self.y_speed = speed * sqrt(0.5)

            else:
                self.x_speed = speed
                self.y_speed = 0

        elif "Up" in curr_keys:
            if "Down" in curr_keys:
                self.y_speed = 0

            else:
                self.y_speed = -1 * speed
                self.x_speed = 0

        elif "Down" in curr_keys:
            self.y_speed = speed
            self.x_speed = 0

        else:
            self.x_speed = 0
            self.y_speed = 0
