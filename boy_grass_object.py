from mimetypes import read_mime_types

from pico2d import *
import random

class Grass:
    def __init__(self):
        # 생성자 함수 : 객체의 초기 상태를 설정
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x,self.y = random.randint(0,700),90
        self.frame = random.randint(0,3)
        self.image = load_image('run_animation1.png')
        self.index = 0

    def update(self):
        global running

        self.frame = (self.frame+1)%3
        self.index = random.randint(0,3)
        self.x+=self.index


    def draw(self):
        self.image.clip_draw(self.frame*64, 64, 64, 64, self.x, self.y, 128,128)

class Smallball:
    def __init__(self):
        self.x,self.y = random.randint(0,700),599
        self.frame = random.randint(0,3)
        self.image = load_image('ball21x21.png')
        self.index = 0

    def update(self):
        global running

        self.frame = (self.frame+1)%3
        self.index = random.randint(0,3)
        self.y-=self.index
        if (self.y < 50):
            self.y = 50


    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y, 21, 21)

class Bigball:
    def __init__(self):
        self.x,self.y = random.randint(0,700),599
        self.frame = random.randint(0,3)
        self.image = load_image('ball41x41.png')
        self.index = 0

    def update(self):
        global running

        self.frame = (self.frame+1)%3
        self.index = random.randint(0,3)
        self.y-=self.index
        if(self.y < 60):
            self.y= 60

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y, 41, 41)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global boy
    global team
    global smallball
    global smallteam
    global bigball
    global bigteam

    running = True
    grass = Grass()
    team = [Boy() for i in range(11)]

    a = random.randint(0,20)

    smallteam = [Smallball() for i in range(a)]
    bigteam = [Bigball() for i in range(20-a)]

def update_world():
    grass.update()
    for boy in team:
        boy.update()

    for smallball in smallteam:
        smallball.update()

    for bigball in bigteam:
        bigball.update()

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for smallball in smallteam:
        smallball.draw()
    for bigball in bigteam:
        bigball.draw()

    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()#상호작용을 시뮬레이션
    render_world()#그 결과 보여줌
    delay(0.05)

close_canvas()
