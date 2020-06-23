from pygame import image, draw

t1 = image.load("tower_images/watch.png")
t2 = image.load("tower_images/canon.png")
t3 = image.load("tower_images/scout.png")
t4 = image.load("tower_images/ancient.png")
t5 = image.load("tower_images/spirit.png")

watch = t1.get_rect()
canon = t2.get_rect()
scout = t3.get_rect()
ancient = t4.get_rect()
spirit = t5.get_rect()


class Tower():
    def __init__(self,x,y,size,type,dmg,range,area,color):
        self.x = x
        self.y = y
        self.type = type
        self.size = size
        self.damage = dmg
        self.range_rate = range
        self.area = area
        self.color = color
        
    def shot(self, canvas, enemy):
        possible_enemy = []
        for each in enemy:
            if (((self.x-each.x)**2)+((self.y-each.y)**2))**(1/2) <= self.range_rate and (self.area == each.type or self.area == "L&A"):
                possible_enemy.append(each)
        if len(possible_enemy) != 0:
            if possible_enemy[0].y > possible_enemy[0].r:
                draw.line(canvas, self.color, (self.x,self.y), (possible_enemy[0].x, possible_enemy[0].y),3)
                possible_enemy[0].health -= self.damage
        
    def show(self, canvas):
        position = (self.x-int(self.size/2),self.y-int(self.size/2),self.size,self.size)

        if self.type == "wt":
            canvas.blit(t1, position)
        elif self.type == "c":
            canvas.blit(t2, position)
        elif self.type == "st":
            canvas.blit(t3, position)
        elif self.type == "at":
            canvas.blit(t4, position)
        elif self.type == "spt":
            canvas.blit(t5, position)
 
        