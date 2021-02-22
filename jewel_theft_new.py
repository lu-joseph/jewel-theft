from tkinter import *
from random import *
from time import *
from math import *
import clock, player, guard, jewel, button


# global constants
root = Tk()
screen = Canvas(root, width=800, height=800, background="white")
screen.pack()
easy_difficulty = 0
medium_difficulty = 1
hard_difficulty = 2


def main():
    global curr_menu
    curr_menu = ""
    root.after(0,start_menu)

    screen.bind("<Any-KeyPress>",key_press)
    screen.bind("<Any-KeyRelease>",key_release)
    screen.bind("<Button-1>",left_click)            

    screen.focus_set()


def run_game():
    global screen_player
    set_init_values()
    while game_running:
        screen_player = player1.draw(curr_keys, game_clock, screen)
        player1.update_speed(curr_keys)
        check_jewel_collision()
        check_key_collision()
        draw_guards()
        guard_movement()
        player1.update_pos()
        update_guard_pos()
        game_clock.update_clock(game_difficulty, game_paused, player1.got_caught)
        draw_misc()
        update_sleep_delete()
        wall_collision()
        game_clock.update_frame_count()
    game_over()


def set_init_values():
    global player1
    player1 = player.Player()

    import_player_sprites()
    import_guard_sprites()

    global jewel_list,jewel_locations,jewel_icon,jewel_case_bars
    global x_big_jewel,y_big_jewel
    jewel_list = []
    jewel_locations = [
        [(73,249),(593,609),(233,489),(73,370),(712,250),(712,730)],
        [(432,369),(552,531),(272,529),(112,690),(712,689),(432,690),(712,410),
         (552,250)],
        [(73,249),(593,609),(233,489),(73,370),(73,490),(73,608),(593,489),
         (354,609),(712,730),(192,249),(311,249),(431,249)]
        ]
    jewel_icon = 0
    jewel_case_bars = [0,0,0,0,0,0,0]
    big_jewel_pos = [(430, 727), (511, 368), (591, 250)]
    x_big_jewel = big_jewel_pos[game_difficulty][0]
    y_big_jewel = big_jewel_pos[game_difficulty][1]

    global x_key,y_key,key_icon,screen_key
    key_pos = [(650, 730), (710, 250), (72, 729)]
    x_key = key_pos[game_difficulty][0]
    y_key = key_pos[game_difficulty][1]
    key_icon = 0
    screen_key = 0

    global pause_menu,win_screen
    pause_menu = 0
    win_screen = 0

    global walls,wall_thickness
    # form: [(x1, y1), (x2, y2)]
    # walls consists of coordinates for lines with specified thickness
    walls = [
        # easy difficulty
        [[(25,300),(165,300)],[(135,425),(280,425)],[(25,540),(165,540)],
         [(300,290),(300,540)],[(305,545),(365,545)],[(135,665),(665,665)],
         [(660,330),(660,665)],[(535,190),(535,545)],[(490,545),(535,545)]],
        # medium difficulty
        [[(190,190),(190,300)],[(190,415),(190,615)],[(190,615),(370,615)],
         [(350,300),(350,445)],[(350,445),(635,445)],[(635,190),(635,445)],
         [(495,610),(635,610)]],
        # hard difficulty
        [[(663,190),(663,318)],[(280,318),(663,318)],[(151,304),(151,681)],
         [(151,442),(399,442)],[(399,442),(399,543)],[(286,560),(286,665)],
         [(286,661),(662,661)],[(662,440),(662,662)],[(538,440),(662,440)],
         [(538,440),(538,543)]]
        ]
    wall_difficulty_thickness = [15, 20, 10]
    wall_thickness = wall_difficulty_thickness[game_difficulty]
    
    global screen_clock,game_clock,score_text,game_running
    screen_clock = 0
    game_clock = clock.Clock()
    game_running = True
    score_text = 0

    global floor,door
    floor = 0
    door = 0

    player1.set_starting_pos(game_difficulty)

    draw_map()
    draw_jewels()
    draw_key()


#------------------------------Importing images-------------------------------#
def import_images():
    global key_image,small_jewel_image,big_jewel_image

    global menu_image,difficulty_image,instructions_image
    global pause_menu_image,win_screen_image,lose_screen_image

    global easy_map,medium_map,hard_map

    key_image = PhotoImage(file="items/key.gif")
    small_jewel_image = PhotoImage(file="items/small_jewel.gif")
    big_jewel_image = PhotoImage(file="items/big_jewel.gif")

    menu_image = PhotoImage(file="menus/menu_screen.gif")
    difficulty_image = PhotoImage(file="menus/difficulty_screen.gif")
    instructions_image = PhotoImage(file="menus/instructions_screen.gif")

    pause_menu_image = PhotoImage(file="menus/pause_menu.gif")
    win_screen_image = PhotoImage(file="menus/win_screen.gif")
    lose_screen_image = PhotoImage(file="menus/lose_screen.gif")
    
    easy_map = PhotoImage(file="maps/easy_map.gif")
    medium_map = PhotoImage(file="maps/medium_map.gif")
    hard_map = PhotoImage(file="maps/hard_map.gif")


def import_player_sprites():
    player1.import_images()


def import_guard_sprites():
    global guard_list, guard_intersections
    global guard_run_right, guard_run_left, guard_run_up, guard_run_down
    guard_list = []
    guard_intersections = []  # consists of coordinates for boxes representing intersections
    guard_run_right = []
    guard_run_left = []
    guard_run_up = []
    guard_run_down = []

    run_frames = 9
    run_sprites = [guard_run_right, guard_run_left, guard_run_up, guard_run_down]
    run_files = ["sprites/guard_run_right.gif", "sprites/guard_run_left.gif",
                  "sprites/guard_run_up.gif", "sprites/guard_run_down.gif"]
    for i in range(len(run_sprites)):
        for j in range(run_frames):
            frame_text = "gif -index " + str(j)
            image = PhotoImage(file = run_files[i],format = frame_text)
            run_sprites[i].append(image)

    if game_difficulty == easy_difficulty:
        g1 = guard.Guard(500, 730, 1, 1, False)
        g2 = guard.Guard(300, 730, -1, -1, False)
        guard_list = [g1, g2]
        #format: [(x1, y1),(x2, y2)]
        guard_intersections = [
            [(595,725),(605,735)],[(715,725),(725,735)],[(715,245),(725,255)],
            [(585,245),(595,255)],[(585,595),(595,605)],[(80,725),(90,735)],
            [(80,595),(90,605)],[(215,595),(225,605)],[(215,480),(225,490)],
            [(80,480),(90,490)],[(80,360),(90,370)],[(215,360),(225,370)],
            [(215,240),(225,250)],[(80,240),(90,250)]
            ]

    elif game_difficulty == medium_difficulty:
        g1 = guard.Guard(710, 260, -1, 1, True)
        g2 = guard.Guard(430, 250, -1, -1, False)
        guard_list = [g1, g2]
        #format: [(x1, y1),(x2, y2)]
        guard_intersections = [
            [(265,243),(275,253)],[(265,525),(275,535)],[(547,525),(557,535)],
            [(706,725),(716,735)],[(427,725),(437,735)],[(427,525),(437,535)],
            [(706,243),(716,253)],[(506,243),(516,253)]
            ]
        
    elif game_difficulty == hard_difficulty:
        g1 = guard.Guard(472, 250, -1, 1, False)
        g2 = guard.Guard(70, 730, 1, -1, True)
        g3 = guard.Guard(351, 529, 1, -1, True)
        g4 = guard.Guard(231, 529, -1, -1, False)
        guard_list = [g1, g2, g3, g4]
        #format: [(x1, y1),(x2, y2)]
        guard_intersections = [
            [(705,725),(715,735)],[(65,725),(75,735)],[(65,245),(75,255)],
            [(705,362),(715,372)],[(467,362),(477,372)],[(467,603),(477,612)],
            [(226,725),(236,735)],[(226,362),(236,372)],[(226,245),(236,255)],
            [(467,245),(477,255)],[(705,245),(715,255)],[(226,524),(236,534)],
            [(346,524),(356,534)],[(346,603),(356,612)],[(586,603),(596,612)],
            [(586,524),(596,534)]
            ]


#-------------------------------Player inputs---------------------------------#
def key_press(event):
    global game_running
    if event.keysym not in curr_keys:
        curr_keys.append(event.keysym)

    if game_paused:
        if event.keysym == "q":
            game_running = False

        if event.keysym == "r":
            restart_game()

    if curr_menu == "" and event.keysym == "p":
        pause_game()


def key_release(event):
    while event.keysym in curr_keys:
        curr_keys.remove(event.keysym)


def left_click(event):
    global curr_menu,game_difficulty

    x_mouse = event.x
    y_mouse = event.y

    pause_quit = button.Button(184, 423, 365, 510)
    pause_restart = button.Button(425, 423, 615, 510)
    start_difficulty = button.Button(55, 605, 345, 745)
    start_instructions = button.Button(440, 605, 745, 745)
    instructions_start = button.Button(56, 607, 755, 745)
    win_quit = button.Button(55, 607, 345, 744)
    win_start = button.Button(439, 607, 744, 744)
    lose_quit = button.Button(55, 607, 345, 744)
    lose_start = button.Button(439, 607, 744, 744)
    difficulty_easy = button.Button(255, 80, 545, 215)
    difficulty_medium = button.Button(255, 325, 545, 465)
    difficulty_hard = button.Button(255, 580, 545, 720)
    difficulty_start = button.Button(55, 80, 200, 170)

    if game_paused:
        if pause_quit.check_press(x_mouse, y_mouse):
            quit_game()
        elif pause_restart.check_press(x_mouse, y_mouse):
            restart_game()

    if curr_menu == "start":
        if start_difficulty.check_press(x_mouse, y_mouse):
            choose_difficulty()
        elif start_instructions.check_press(x_mouse, y_mouse):
            instructions()
    elif curr_menu == "instructions":
        if instructions_start.check_press(x_mouse, y_mouse):
            start_menu()
    elif curr_menu == "win":
        if win_quit.check_press(x_mouse, y_mouse):
            quit_game()
        if win_start.check_press(x_mouse, y_mouse):
            start_menu()
    elif curr_menu == "lose":
        if lose_quit.check_press(x_mouse, y_mouse):
            quit_game()
        if lose_start.check_press(x_mouse, y_mouse):
            start_menu()
    elif curr_menu == "difficulty":
        if difficulty_easy.check_press(x_mouse, y_mouse):
            game_difficulty = easy_difficulty
            screen.delete(difficulty_screen)
            curr_menu = ""
            run_game()
        elif difficulty_medium.check_press(x_mouse, y_mouse):
            game_difficulty = medium_difficulty
            screen.delete(difficulty_screen)
            curr_menu = ""
            run_game()
        elif difficulty_hard.check_press(x_mouse, y_mouse):
            game_difficulty = hard_difficulty
            screen.delete(difficulty_screen)
            curr_menu = ""
            run_game()
        elif difficulty_start.check_press(x_mouse, y_mouse):
            start_menu()


#----------------------------Menu procedures----------------------------------#  
def start_menu():
    global main_menu_screen,curr_menu,curr_keys,game_paused

    if curr_menu == "instructions":
        screen.delete(instructions_screen)
    elif curr_menu == "win":
        screen.delete(win_screen, time_text)
    elif curr_menu == "lose":
        screen.delete(lose_screen)
    elif curr_menu == "difficulty":
        screen.delete(difficulty_screen)

    import_images()
    game_paused = False
    curr_menu = "start"
    curr_keys = []
    main_menu_screen = screen.create_image(400,400,image=menu_image)


def instructions():
    global curr_menu,instructions_screen
    screen.delete(main_menu_screen)
    curr_menu = "instructions"
    instructions_screen = screen.create_image(400,400,image=instructions_image)


def choose_difficulty():
    global difficulty_screen,curr_menu
    screen.delete(main_menu_screen)
    curr_menu = "difficulty"
    difficulty_screen = screen.create_image(400,400,image=difficulty_image)


def quit_game():
    root.destroy()


def restart_game():
    global game_paused
    screen.delete(screen_player,score_text,screen_clock,floor)
    
    for i in range(len(jewel_list)):
        screen.delete(jewel_list[i])

    for i in range(len(guard_list)):
        screen.delete(guard_list[i].drawing)
        screen.delete(guard_list[i].flashlight)

    for i in jewel_case_bars:
        screen.delete(i)

    if game_paused:
        screen.delete(pause_menu)
        game_paused = False

    if player1.got_jewel:
        screen.delete(door)
    
    set_init_values()


def pause_game():
    global game_paused,pause_menu,guard_list
    if game_paused:
        game_paused = False

        player1.walk_speed = 7
        player1.run_speed = 15

        for i in range(len(guard_list)):
            guard_list[i].x_speed = 10
            guard_list[i].y_speed = 10            

        screen.delete(pause_menu)

    else:
        game_paused = True
        player1.walk_speed = 0
        player1.run_speed = 0
        
        for i in range(len(guard_list)):
            guard_list[i].x_speed = 0
            guard_list[i].y_speed = 0


def game_over():
    global lose_screen,curr_menu
    if player1.won:
        player1.score = game_clock.calculate_bonus(player1.score)
        show_win_screen()

    else:
        if player1.got_caught:            
            lose_screen = screen.create_image(400,400,image=lose_screen_image)
            curr_menu = "lose"

        else:
            quit_game()


def show_win_screen():
    global jewel_icon,score_text,curr_menu,win_screen,time_text
    curr_menu = "win"
    win_screen = screen.create_image(400,400,image=win_screen_image)
    time_taken = "Time taken: " + str(game_clock.time_string)
    score_addition = "Time bonus: " + str(game_clock.time_bonus) + \
                    " Final score: " + str(player1.score)
    time_text = screen.create_text(
        400, 190, anchor=CENTER, text=time_taken, font="fixedsys 20", fill="white"
        )
    score_text = screen.create_text(
        400, 220, anchor=CENTER, text=score_addition, font="fixedsys 20",fill="white"
        )


def update_sleep_delete():   
    screen.update()
    sleep(0.03)
    screen.delete(screen_player,screen_clock,score_text,key_icon,jewel_icon)

    for i in range(len(guard_list)):
        screen.delete(guard_list[i].drawing)
        screen.delete(guard_list[i].flashlight)

    if game_paused:
        screen.delete(pause_menu)

    if player1.got_jewel:
        screen.delete(door)


#----------------------------Guard procedures---------------------------------#
def guard_movement():
    for i in range(len(guard_list)):
        guard_list[i].update_movement(game_difficulty, guard_intersections, i)


def update_guard_pos():
    for i in range(len(guard_list)):
        guard_list[i].update_pos()


#-----------------------------Drawing procedures------------------------------#      
def draw_guards():
    global game_running
    for i in range(len(guard_list)):
        if not game_running:
            break

        # .draw() method returns False if player is caught,
        #   setting game_running to False
        game_running = guard_list[i].draw(
            game_difficulty, guard_intersections, screen, player1, game_paused,
            game_clock, guard_run_right, guard_run_left, guard_run_up,
            guard_run_down, guard_list
            )


def draw_jewels():
    if game_difficulty == easy_difficulty:
        num_jewels = 3

    elif game_difficulty == medium_difficulty:
        num_jewels = 4

    elif game_difficulty == hard_difficulty:
        num_jewels = 6

    # for each jewel, its location will be randomly picked and removed the list
    #   of possible locaitons and then drawn
    for i in range(num_jewels):
        location = choice(jewel_locations[game_difficulty])
        j = jewel.Jewel(location[0], location[1], False)
        j.screen_jewel = screen.create_image(
            j.x, j.y, anchor=CENTER, image=small_jewel_image
            )
        jewel_list.append(j)
        jewel_locations[game_difficulty].remove(location)

    big_jewel = jewel.Jewel(x_big_jewel, y_big_jewel, True)
    big_jewel.screen_jewel = screen.create_image(
        x_big_jewel, y_big_jewel, anchor=CENTER, image=big_jewel_image
        )
    jewel_list.append(big_jewel)

    #draws a jewel case if the key hasn't been obtained yet
    if player1.got_key == False:
        x = -20
        y = -20
        
        for i in range(5):
            jewel_case_bars[i] = screen.create_line(
                big_jewel.x + x, big_jewel.y - 20,
                big_jewel.x + x, big_jewel.y + 20,fill="grey",width=3
                )
            x += 10
            
        x = -20
        
        for i in range(2):
            bar = screen.create_line(
                big_jewel.x - 20, big_jewel.y + y,
                big_jewel.x + 20, big_jewel.y + y,
                fill="grey",width=3
                )
            jewel_case_bars.append(bar)
            y += 40

      
def draw_key():
    global screen_key
    screen_key = screen.create_image(x_key,y_key,anchor=CENTER,image=key_image)


def draw_map():
    global floor

    if game_difficulty == easy_difficulty:
        floor = screen.create_image(400,400,image=easy_map)

    elif game_difficulty == medium_difficulty:
        floor = screen.create_image(400,400,image=medium_map)

    elif game_difficulty == hard_difficulty:
        floor = screen.create_image(400,400,image=hard_map)


def draw_misc():
    global score_text, key_icon, jewel_icon, pause_menu, door
    global game_clock, screen_clock

    score_text = screen.create_text(
        120, 132, anchor=CENTER, text=player1.score,
        fill="white",font="comicsans 30"
        )

    # draws an icon for the key if it has been obtained
    if player1.got_key:
        key_icon = screen.create_image(220,140,anchor=CENTER,image=key_image)

    # draws an icon for the jewel and highlights the door if the red jewel
    #   has been obtained
    if player1.got_jewel:
        jewel_icon = screen.create_image(
            570, 135, anchor=CENTER, image=big_jewel_image
            )
        # form: (x1, y1, x2, y2)
        door_locations = [
            (368, 184, 495, 191), (48, 184, 136, 191), (688, 184, 767, 191)
            ]
        chosen_door = door_locations[game_difficulty]
        door = screen.create_rectangle(
            chosen_door[0], chosen_door[1], chosen_door[2], chosen_door[3],
            fill="green", outline="green"
            )

    screen_clock = game_clock.draw_time(screen)
    
    #draws pause menu
    if game_paused:
        pause_menu = screen.create_image(400,400,image=pause_menu_image)


#----------------------------Collision procedures-----------------------------# 
def check_jewel_collision():
    for i in range(len(jewel_list)):
        jewel_list[i].check_collision(player1, screen)


def check_key_collision():    
    distance = sqrt((x_key-player1.x)**2 + (y_key-player1.y)**2)

    if distance <= 35:
        screen.delete(screen_key)
        player1.got_key = True

        for i in jewel_case_bars:
            screen.delete(i)
  

def wall_collision():
    global game_running
    
    if player1.x - player1.width <= 30: 
        player1.x = 30 + player1.width
        player1.x_speed = 0

    if player1.x + player1.width >= 770:
        player1.x = 770 - player1.width
        player1.x_speed = 0

    if player1.y-player1.height <= 180:
        if game_difficulty == easy_difficulty:
            if player1.got_jewel and 368 <= player1.x <= 495:
                game_running = False
                player1.won = True

            else:
                player1.y = 180 + player1.height
                player1.y_speed = 0
                
        elif game_difficulty == medium_difficulty:
            if player1.got_jewel and 48 <= player1.x <= 136:
                game_running = False
                player1.won = True

            else:
                player1.y = 180 + player1.height
                player1.y_speed = 0

        elif game_difficulty == hard_difficulty:
            if player1.got_jewel and 688 <= player1.x <= 767:
                game_running = False
                player1.won = True

            else:
                player1.y = 180 + player1.height
                player1.y_speed = 0

    if player1.y+player1.height >= 780:
        player1.y = 780 - player1.height
        player1.y_speed = 0
    
    for i in range(len(walls[game_difficulty])):
        if walls[game_difficulty][i][0][0] - walls[game_difficulty][i][0][1] == 0:
            wallVert = True

        else:
            wallVert = False

        if wallVert:
            if (walls[game_difficulty][i][0][0] - player1.width - wall_thickness / 2)\
               <= player1.x <= \
               (walls[game_difficulty][i][0][0] + player1.width + wall_thickness / 2):

                if (walls[game_difficulty][i][0][1] - player1.height) <= \
                   player1.y <= walls[game_difficulty][i][0][1]:

                    player1.y = walls[game_difficulty][i][0][1] - player1.height
                    player1.y_speed = 0

                elif walls[game_difficulty][i][1][1] <= player1.y \
                     <= (walls[game_difficulty][i][1][1] + player1.height):

                    player1.y = walls[game_difficulty][i][1][1] + player1.height
                    player1.y_speed = 0

            if (walls[game_difficulty][i][0][1] - player1.height) <= player1.y\
               <= (walls[game_difficulty][i][1][1] + player1.height):

                if (walls[game_difficulty][i][0][0] + wall_thickness/2) \
                   <= player1.x <= (walls[game_difficulty][i][0][0] + \
                                    wall_thickness/2 + player1.width):

                    player1.x = walls[game_difficulty][i][0][0] + \
                                wall_thickness/2 + player1.width
                    player1.x_speed = 0

                elif (walls[game_difficulty][i][0][0] - \
                      wall_thickness/2 - player1.width)\
                     <= player1.x <= (walls[game_difficulty][i][0][0] - wall_thickness/2):

                    player1.x = walls[game_difficulty][i][0][0] - wall_thickness/2 - player1.width
                    player1.x_speed = 0

        else: 
            if (walls[game_difficulty][i][0][0] - player1.width) <= player1.x \
               <= (walls[game_difficulty][i][1][0] + player1.width):

                if (walls[game_difficulty][i][0][1] - wall_thickness/2 - player1.height)\
                   <= player1.y <= (walls[game_difficulty][i][0][1] - wall_thickness/2):
    
                    player1.y = walls[game_difficulty][i][0][1] - wall_thickness/2 - player1.height
                    player1.y_speed = 0

                elif (walls[game_difficulty][i][1][1] + wall_thickness/2) <= player1.y \
                     <= (walls[game_difficulty][i][1][1] + wall_thickness/2 + player1.height):

                    player1.y = walls[game_difficulty][i][1][1] + wall_thickness/2 + player1.height
                    player1.y_speed = 0

            if (walls[game_difficulty][i][0][1] - wall_thickness/2 - player1.height)\
               <= player1.y <= \
               (walls[game_difficulty][i][1][1] + wall_thickness/2 + player1.height):

                if walls[game_difficulty][i][1][0] <= player1.x <= \
                   (walls[game_difficulty][i][1][0] + player1.width):

                    player1.x = walls[game_difficulty][i][1][0] + player1.width
                    player1.x_speed = 0

                if (walls[game_difficulty][i][0][0] - player1.width) <= player1.x \
                   <= walls[game_difficulty][i][0][0]:

                    player1.x = walls[game_difficulty][i][0][0] - player1.width
                    player1.x_speed = 0


if __name__ == "__main__":
    main()
