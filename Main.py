from pygame import init, display, mouse, event, MOUSEBUTTONDOWN, QUIT, Rect
from gamefield import *
from tower import *
from sys import exit


# Game initialisation
init()

# Creating canvas
screen = display.set_mode((1000,890))
display.set_caption("Tower Defence")

# Variables
enemies = None
tower_choice = 0
tower_type = None
towers = []


while True:
    screen.fill([25,150,0])
    draw_gamefield(screen)
    mouse_x = mouse.get_pos()[0]
    mouse_y = mouse.get_pos()[1]
    
    if enemies != None:
        if len(enemies) != 0:
            wave_state = is_wave(screen, towers, enemies)
        else:
            print("WAVE DEFEATED!")
            enemies = None
    
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            exit()
        # For Next wave button
        elif ev.type == MOUSEBUTTONDOWN and ev.pos[0]>825 and ev.pos[0]<991 and ev.pos[1]>820 and ev.pos[1]<880:
            if ev.button == 1:
                enemies = button(ev.pos, Rect((825,820),(991,880)), screen, tower_choice, towers)
        elif ev.type == MOUSEBUTTONDOWN and ev.pos[0]>825 and ev.pos[0]<875 and ev.pos[1]>170 and ev.pos[1]<220:
            if ev.button == 1:
                tower_type = button(ev.pos, Rect((825,170),(875,220)), screen, tower_choice, towers)
        elif ev.type == MOUSEBUTTONDOWN and ev.pos[0]>825 and ev.pos[0]<875 and ev.pos[1]>300 and ev.pos[1]<350:
            if ev.button == 1:
                tower_type = button(ev.pos, Rect((825,300),(875,350)), screen, tower_choice, towers)
        elif ev.type == MOUSEBUTTONDOWN and ev.pos[0]>825 and ev.pos[0]<875 and ev.pos[1]>430 and ev.pos[1]<480:
            if ev.button == 1:
                tower_type = button(ev.pos, Rect((825,430),(875,480)), screen, tower_choice, towers)
        elif ev.type == MOUSEBUTTONDOWN and ev.pos[0]>825 and ev.pos[0]<875 and ev.pos[1]>560 and ev.pos[1]<610:
            if ev.button == 1:
                tower_type = button(ev.pos, Rect((825,560),(875,610)), screen, tower_choice, towers)
        elif ev.type == MOUSEBUTTONDOWN and ev.pos[0]>825 and ev.pos[0]<875 and ev.pos[1]>690 and ev.pos[1]<740:
            if ev.button == 1:
                tower_type = button(ev.pos, Rect((825,690),(875,740)), screen, tower_choice, towers)
        elif ev.type == MOUSEBUTTONDOWN and tower_type != None:
            if is_grass(mouse_x,mouse_y,40) == True and is_taken(mouse_x,mouse_y,towers) == False:
                if tower_type == "wt":
                    towers.append(Tower(mouse_x,mouse_y,40,tower_type,10,200,"L",[255,255,255]))
                elif tower_type == "c":
                    towers.append(Tower(mouse_x,mouse_y,40,tower_type,50,200,"L",[210,210,210]))
                elif tower_type == "st":
                    towers.append(Tower(mouse_x,mouse_y,40,tower_type,25,200,"A",[0,170,255]))
                elif tower_type == "at":
                    towers.append(Tower(mouse_x,mouse_y,40,tower_type,100,300,"L&A",[255,170,255]))
                elif tower_type == "spt":
                    towers.append(Tower(mouse_x,mouse_y,40,tower_type,200,450,"L&A",[160,100,205]))
                tower_type = None
    
    for tower in towers:
        tower.show(screen)
        
    if mouse_x > 825 and mouse_x < 991 and mouse_y > 820 and mouse_y < 880:
            screen.blit(font.SysFont("Helvetica", 50).render("NEXT", False, [100,255,100]), (842,822))

    display.update()