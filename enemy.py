from pygame import draw

class Enemy():
    def __init__(self,x,y,r,health,type):
        self.x = x
        self.y = y
        self.r = r
        self.full_health = health
        self.health = health
        self.type = type
        self.step = 2
    
    def show(self,canvas):
        health_percent = self.health/self.full_health*100
        red = 255-int(round(255/100*health_percent))

        if self.type == "L":
            green = 255-red
            draw.circle(canvas, [red, green, 0], (self.x,self.y), self.r)
        if self.type == "A":
            blue = 255-red
            draw.circle(canvas, [red, 0, blue], (self.x,self.y), self.r)
            
    def move_Up(self,canvas):
        self.y -= self.step
        
    def move_Down(self,canvas):
        self.y += self.step
        
    def move_Left(self,canvas):
        self.x -= self.step
        
    def move_Right(self,canvas):
        self.x += self.step

    def is_dead(self):
        if self.health <= 0:
            return True