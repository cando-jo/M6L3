#pgzero

WIDTH = 600
HEIGHT = 400
FPS = 30
TITLE = "Clicker Game"

arkaplan = Actor("arkaplan")
zurafa  = Actor("zürafa", (150, 250))
bonus1 = Actor("bonus", (450, 100))
bonus2 = Actor("bonus", (450, 200))
puan = 0
tiklama = 1

def draw():
    arkaplan.draw()
    bonus1.draw()
    bonus2.draw()
    zurafa.draw()
    screen.draw.text(puan, center=(150, 100), color="white", fontsize=96)
    
    screen.draw.text("Her 2 saniye için 1$", center=(450, 80), color="black", fontsize=20)
    screen.draw.text("Ücret: 15 Puan", center=(450, 110), color="black", fontsize=20)
    
    screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize=20)
    screen.draw.text("Ücret: 200 Puan", center=(450, 210), color="black", fontsize=20)
    
def on_mouse_down(button, pos):
    global puan
    
    if button == mouse.LEFT:
        if bonus1.collidepoint(pos) and puan >= 15:
            puan -= 15
            schedule_interval(bonus_1_icin, 2)
            
        if bonus1.collidepoint(pos) and puan >= 200:
            puan -= 200
            schedule_interval(bonus_2_icin, 2)
            
            
        if zurafa.collidepoint(pos):
            zurafa.y = 200
            animate(zurafa, tween='bounce_end', duration=0.5, y=250)
            puan = puan + tiklama
            
def bonus_1_icin():
    global puan
    puan += 1

def bonus_2_icin():
    global puan
    puan += 15
