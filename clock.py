from time import *

# constants
easy_difficulty = 0
medium_difficulty = 1
hard_difficulty = 2


class Clock:
    def __init__(self):
        self.game_clock = 0
        self.start_time = time()
        self.time_bonus = 1000
        self.time_string = "00:00"
        self.frame_count = 0

    def update_clock(self, game_difficulty, game_paused, player_caught):
        if not game_paused and not player_caught:
            elapsed_time = time() - self.start_time

            if elapsed_time >= 1.0:
                self.game_clock += 1
                self.start_time = time()
                time_bonus_increments = [10, 20, 25]
                self.time_bonus -= time_bonus_increments[game_difficulty]

    def update_frame_count(self):
        self.frame_count += 1

    # returns a new value of score for the player
    def calculate_bonus(self, score):
        self.time_bonus = max(0, self.time_bonus)
        return score + self.time_bonus

    # returns a screen.create_text object for the time
    def draw_time(self, screen):
        if self.game_clock < 10:
            self.time_string = "00:0" + str(self.game_clock)

        elif self.game_clock >= 60:
            num_mins = int(self.game_clock / 60)
            num_secs = self.game_clock - num_mins * 60

            if num_mins >= 10:
                min_part = str(num_mins)

            else:
                min_part = "0" + str(num_mins)

            if num_secs >= 10:
                sec_part = str(num_secs)

            else:
                sec_part = "0" + str(num_secs)

            self.time_string = min_part + ":" + sec_part
    
        else:
            self.time_string = "00:" + str(self.game_clock)

        return screen.create_text(
            680,132,text=self.time_string,font="comicsans 25",fill="white"
            )
