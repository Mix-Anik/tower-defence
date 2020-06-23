from pygame import draw, font
from enemy import Enemy

gold = 500
lives = 20
wave = "1"
coef = 1

black = [0,0,0]
brown = [255,228,171]
green = [25,150,0]
neon_green = [100,255,100]
white = [250,250,250]
gray1 = [80,80,80]
gray2 = [125,125,125]
gray3 = [210,210,210]
golden = [255,200,0]
cyan = [0,255,255]
orange = [255,120,0]
red = [255,0,0]
blue = [0,170,255]
pink = [255,170,255]
purple = [160,100,205]

def button(cur, rect, canvas, type, towers):
    global gold
    global wave
    global lives
    if cur[0]>825 and cur[0]<991 and cur[1]>820 and cur[1]<880 and rect.collidepoint(cur):
        if wave == "1":
            print("WAVE 1 INCOMING!")
            wave = 1
            type = wave_start(canvas, 10, towers, 750, "L")  
        else:
            wave += 1
            print("WAVE " + str(wave) + " INCOMING!")
            enemies = 10 + 5*(wave // 5)
            if wave % 4 == 0:
                type = wave_start(canvas,enemies, towers, (1+0.2*wave)*750, "A")
            else:
                type = wave_start(canvas,enemies, towers, (1+0.2*wave)*750, "L")
    elif cur[0]>825 and cur[0]<875 and cur[1]>170 and cur[1]<220 and rect.collidepoint(cur):
        if gold >= 15:
            type = "wt"
            print("Bought Watch Tower")
            gold -= 15
        else:
            print("Not Enough Gold!")
    elif cur[0]>825 and cur[0]<875 and cur[1]>300 and cur[1]<350 and rect.collidepoint(cur):
        if gold >= 50:
            type = "c"
            print("Bought Cannon")
            gold -= 50
        else:
            print("Not Enough Gold!")
    elif cur[0]>825 and cur[0]<875 and cur[1]>430 and cur[1]<480 and rect.collidepoint(cur):
        if gold >= 30:
            type = "st"
            print("Bought Scout Tower")
            gold -= 30
        else:
            print("Not Enough Gold!")
    elif cur[0]>825 and cur[0]<875 and cur[1]>560 and cur[1]<610 and rect.collidepoint(cur):
        if gold >= 100:
            type = "at"
            print("Bought Ancient Tower")
            gold -= 100
        else:
            print("Not Enough Gold!")
    elif cur[0]>825 and cur[0]<875 and cur[1]>690 and cur[1]<740 and rect.collidepoint(cur):
        if gold >= 400:
            type = "spt"
            print("Bought Spirit Tower")
            gold -= 400
        else:
            print("Not Enough Gold!")
    return type
          
def draw_gamefield(screen):
    road = [(195,0),(195,20),(20,20),(20,470),
        (320,470),(320,320),(495,320),(495,570),
        (20,570),(20,870),(795,870),(795,20),
        (495,20),(495,0),(395,0),(395,120),
        (695,120),(695,770),(120,770),(120,670),
        (595,670),(595,220),(220,220),(220,370),
        (120,370),(120,120),(295,120),(295,0)]
    
    border = [(195,0),(195,20),(20,20),(20,470),
            (320,470),(320,320),(495,320),(495,570),
            (20,570),(20,870),(795,870),(795,20),
            (495,20),(495,0),(395,0),(395,120),
            (695,120),(695,770),(120,770),(120,670),
            (595,670),(595,220),(220,220),(220,370),
            (120,370),(120,120),(295,120),(295,0)]
    draw.polygon(screen, brown, road)

    for i in range(len(border)-1):
        if i != 13:
            draw.line(screen, black, border[i], border[i+1], 5)
    # Dark area on right side
    draw.polygon(screen, gray1, [(810,2),(810,888),(1000,888),(1000,2)])
    draw.polygon(screen, black, [(810,2),(810,888),(1000,888),(1000,2)], 3)
    # Gold, lives and wave area
    draw.polygon(screen, gray2, [(830,20),(830,110),(980,110),(980,20)])
    draw.polygon(screen, black, [(830,20),(830,110),(980,110),(980,20)], 3)
    screen.blit(font.SysFont("Helvetica", 29).render("Gold: "+str(gold), False, golden), (835,19))
    screen.blit(font.SysFont("Helvetica", 29).render("Lives: "+str(lives), False, cyan), (835,49))
    screen.blit(font.SysFont("Helvetica", 29).render("Wave: "+str(wave), False, orange), (835,79))
    # Watch Tower
    screen.blit(font.SysFont("Times", 22).render("Watch Tower", False, white), (880,183))
    draw.polygon(screen, gray2, [(825,170),(825,220),(875,220),(875,170)])
    draw.polygon(screen, black, [(825,170),(825,220),(875,220),(875,170)], 3)
    if gold >= 15:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, neon_green), (829,174))
        screen.blit(font.SysFont("Helvetica", 18).render("15", False, neon_green), (839,195))
    else:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, red), (829,174))
        screen.blit(font.SysFont("Helvetica", 18).render("15", False, red), (839,195))
    # Watch tower stats
    screen.blit(font.SysFont("Helvetica", 20).render("► Land", False, white), (840,225))
    screen.blit(font.SysFont("Helvetica", 20).render("► Damage: 10", False, white), (840,245))
    screen.blit(font.SysFont("Helvetica", 20).render("► Fire Rate: 10", False, white), (840,265))
    
    # Cannon
    screen.blit(font.SysFont("Times", 25).render("Cannon", False, gray3), (880,312))
    draw.polygon(screen, gray2, [(825,300),(825,350),(875,350),(875,300)])
    draw.polygon(screen, black, [(825,300),(825,350),(875,350),(875,300)], 3)
    if gold >= 50:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, neon_green), (829,304))
        screen.blit(font.SysFont("Helvetica", 18).render("50", False, neon_green), (841,325))
    else:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, red), (829,304))
        screen.blit(font.SysFont("Helvetica", 18).render("50", False, red), (841,325))
    # Cannon stats
    screen.blit(font.SysFont("Helvetica", 20).render("► Land", False, white), (840,355))
    screen.blit(font.SysFont("Helvetica", 20).render("► Damage: 50", False, white), (840,375))
    screen.blit(font.SysFont("Helvetica", 20).render("► Fire Rate: 4", False, white), (840,395))
    
    # Scout Tower
    screen.blit(font.SysFont("Times", 22).render("Scout Tower", False, blue), (882,443))
    draw.polygon(screen, gray2, [(825,430),(825,480),(875,480),(875,430)])
    draw.polygon(screen, black, [(825,430),(825,480),(875,480),(875,430)], 3)
    if gold >= 30:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, neon_green), (829,434))
        screen.blit(font.SysFont("Helvetica", 18).render("30", False, neon_green), (840,455))
    else:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, red), (829,434))
        screen.blit(font.SysFont("Helvetica", 18).render("30", False, red), (840,455))
    # Scout Tower stats
    screen.blit(font.SysFont("Helvetica", 20).render("►  Air", False, white), (840,485))
    screen.blit(font.SysFont("Helvetica", 20).render("► Damage: 25", False, white), (840,505))
    screen.blit(font.SysFont("Helvetica", 20).render("► Fire Rate: 8", False, white), (840,525))
    
    # Ancient Tower
    screen.blit(font.SysFont("Times", 20).render("Ancient Tower", False, pink), (878,573))
    draw.polygon(screen, gray2, [(825,560),(825,610),(875,610),(875,560)])
    draw.polygon(screen, black, [(825,560),(825,610),(875,610),(875,560)], 3)
    if gold >= 100:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, neon_green), (829,564))
        screen.blit(font.SysFont("Helvetica", 18).render("100", False, neon_green), (835,585))
    else:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, red), (829,564))
        screen.blit(font.SysFont("Helvetica", 18).render("100", False, red), (835,585))
    # Ancient tower stats
    screen.blit(font.SysFont("Helvetica", 20).render("► Land & Air", False, white), (840,615))
    screen.blit(font.SysFont("Helvetica", 20).render("► Damage: 100", False, white), (840,635))
    screen.blit(font.SysFont("Helvetica", 20).render("► Fire Rate: 7", False, white), (840,655))
    
    # Spirit Tower
    screen.blit(font.SysFont("Times", 22).render("Spirit Tower", False, purple), (882,703))
    draw.polygon(screen, gray2, [(825,690),(825,740),(875,740),(875,690)])
    draw.polygon(screen, black, [(825,690),(825,740),(875,740),(875,690)], 3)
    if gold >= 450:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, neon_green), (829,694))
        screen.blit(font.SysFont("Helvetica", 18).render("450", False, neon_green), (836,715))
    else:
        screen.blit(font.SysFont("Helvetica", 18).render("Cost:", False, red), (829,694))
        screen.blit(font.SysFont("Helvetica", 18).render("450", False, red), (836,715))
    # Spirit tower stats
    screen.blit(font.SysFont("Helvetica", 20).render("► Land & Air", False, white), (840,745))
    screen.blit(font.SysFont("Helvetica", 20).render("► Damage: 200", False, white), (840,765))
    screen.blit(font.SysFont("Helvetica", 20).render("► Fire Rate: 9", False, white), (840,785))
    
    # Next Button
    draw.polygon(screen, gray2, [(825,820),(825,880),(991,880),(991,820)])
    draw.polygon(screen, black, [(825,820),(825,880),(991,880),(991,820)], 3)
    screen.blit(font.SysFont("Helvetica", 50).render("NEXT", False, white), (842,822))

def wave_start(canvas, amount, towers, health, type):
    global gold
    army = []
    y = 0

    for i in range(amount):
        army.append(Enemy(245,y,15,health,type))
        y -= 40
        
    return army

def is_wave(canvas, towers, army):
    global gold
    global lives

    for tower in towers:
        tower.show(canvas)
        tower.shot(canvas,army)

    for enemy in army:
        if enemy.is_dead() == True:
            army.remove(enemy)
            gold += 3

    for enemy in army:
        if enemy.x == 245 and enemy.y < 70:
            enemy.move_Down(canvas)
        elif enemy.x > 71 and enemy.x <= 245 and enemy.y == 70:
            enemy.move_Left(canvas)
        elif enemy.x == 71 and enemy.y < 420 and enemy.y >= 70:
            enemy.move_Down(canvas)
        elif enemy.x < 271 and enemy.x >= 71 and enemy.y == 420:
            enemy.move_Right(canvas)
        elif enemy.x == 271 and enemy.y > 270 and enemy.y <= 420:
            enemy.move_Up(canvas)
        elif enemy.x < 545 and enemy.x >= 271 and enemy.y == 270:
            enemy.move_Right(canvas)
        elif enemy.x == 545 and enemy.y < 620 and enemy.y >= 270:
            enemy.move_Down(canvas)
        elif enemy.x > 71 and enemy.x <= 545 and enemy.y == 620:
            enemy.move_Left(canvas)
        elif enemy.x == 71 and enemy.y < 820 and enemy.y >= 620:
            enemy.move_Down(canvas)
        elif enemy.x < 745 and enemy.x >= 71 and enemy.y == 820:
            enemy.move_Right(canvas)
        elif enemy.x == 745 and enemy.y > 70 and enemy.y <= 820:
            enemy.move_Up(canvas)
        elif enemy.x > 445 and enemy.x <= 745 and enemy.y == 70:
            enemy.move_Left(canvas)
        elif enemy.x == 445 and enemy.y > -20 and enemy.y <= 70:
            enemy.move_Up(canvas)
        elif enemy.x == 445 and enemy.y == -20:
            army.remove(enemy)
            lives -= 1
            
        enemy.show(canvas)
    return army

def is_grass(x,y,t_size):
    if x > 295+t_size/2 and x < 395-t_size/2 and y > 0+t_size/2 and y < 220-t_size/2:
        return True
    elif x > 120+t_size/2 and x < 695-t_size/2 and y > 120+t_size/2 and y < 220-t_size/2:
        return True
    elif x > 120+t_size/2 and x < 220-t_size/2 and y > 120+t_size/2 and y < 370-t_size/2:
        return True
    elif x > 595+t_size/2 and x < 695-t_size/2 and y > 120+t_size/2 and y < 770-t_size/2:
        return True
    elif x > 320+t_size/2 and x < 495-t_size/2 and y > 320+t_size/2 and y < 570-t_size/2:
        return True
    elif x > 20+t_size/2 and x < 495-t_size/2 and y > 470+t_size/2 and y < 570-t_size/2:
        return True
    elif x > 120+t_size/2 and x < 695-t_size/2 and y > 670+t_size/2 and y < 770-t_size/2:
        return True
    else:
        print("You can't place tower here")
        return False
    
def is_taken(x,y,towers):
    state = False

    for tower in towers:
        if x > tower.x-tower.size and x < tower.x+tower.size and y > tower.y-tower.size and y < tower.y+tower.size:
            state = True
    if state == True:
        print("There is a tower placed already")
    return state