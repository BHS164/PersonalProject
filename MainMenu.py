import pygame
import pickle
import sys
import os

if getattr(sys, 'frozen', False):
    Path = sys._MEIPASS
else:
    Path = os.path.dirname(__file__)

pygame.init()

# Screen Size
width = 1000
height = 600
# pygame.image.load('Sprites\881826.png')
#Music
pygame.mixer.music.load('Sound/Town.mp3')

# Screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Adventures of <Insert Name Here>')

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
Dgrey = (105, 105, 105)
yellow = (255, 255, 7)
green = (0, 255, 0)
red = (255, 0, 0)
NC = (13, 211, 2255)
blue = (0, 0, 255)

# Other variables
FPS = 30
fpsClock = pygame.time.Clock()


# Set Background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


MenuBack = pygame.image.load('Sprites\GameBackround.png')
BackGround = Background('Sprites\PlayQuitScreen.png', [0, 0])

# Sprites
gameTitle = pygame.image.load('Sprites\GameTitle.PNG')
button = pygame.image.load('Sprites\Button.png')


# Functions:
# Blit text to the screen
def message(size, msg, colorf, colorb, x, y):
    font = pygame.font.Font('Fonts\BadaboomBB_Reg.ttf', size)
    txt = font.render(msg, True, colorf, colorb)
    box = txt.get_rect()
    box.center = (x, y)
    screen.blit(txt, box)


# Different images for which button you are on

def warGender():
    Picking = True
    OnM = True
    onF = False
    while Picking:
        while OnM:
            screen.fill(white)
            screen.blit(MenuBack, [0, 0])
            file = open('name.pckl', 'rb')
            name = pickle.load(file)
            screen.blit(button, [-180, 227])
            screen.blit(button, [322, 227])
            message(60, 'The Adventures of ' + ''.join(name), blue, NC, width / 2, 60)
            message(50, 'Choose a gender', yellow, NC, width / 2, 120)
            message(55, 'Male', white, NC, width / 4, 500)
            message(30, 'Female', black, NC, width / 4 * 3, 500)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        onF = True
                        OnM = False
        while onF:
            screen.fill(white)
            screen.blit(MenuBack, [0, 0])
            file = open('name.pckl', 'rb')
            name = pickle.load(file)
            screen.blit(button, [-180, 227])
            screen.blit(button, [322, 227])
            message(60, 'The Adventures of ' + ''.join(name), blue, NC, width / 2, 60)
            message(50, 'Choose a gender', yellow, NC, width / 2, 120)
            message(30, 'Male', black, NC, width / 4, 500)
            message(55, 'Female', white, NC, width / 4 * 3, 500)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        OnM = True
                        onF = False


def wizGender():
    picking = True
    onM = True
    OnF = False
    while picking:
        while onM:
            screen.fill(white)
            screen.blit(MenuBack, [0, 0])
            file = open('name.pckl', 'rb')
            name = pickle.load(file)
            screen.blit(button, [-180, 227])
            screen.blit(button, [322, 227])
            message(60, 'The Adventures of ' + ''.join(name), blue, NC, width / 2, 60)
            message(50, 'Choose a gender', yellow, NC, width / 2, 120)
            message(55, 'Male', white, NC, width / 4, 500)
            message(30, 'Female', black, NC, width / 4 * 3, 500)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        OnF = True
                        onM = False
        while OnF:
            screen.fill(white)
            screen.blit(MenuBack, [0, 0])
            file = open('name.pckl', 'rb')
            name = pickle.load(file)
            screen.blit(button, [-180, 227])
            screen.blit(button, [322, 227])
            message(60, 'The Adventures of ' + ''.join(name), blue, NC, width / 2, 60)
            message(50, 'Choose a gender', yellow, NC, width / 2, 120)
            message(30, 'Male', black, NC, width / 4, 500)
            message(55, 'Female', white, NC, width / 4 * 3, 500)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        onM = True
                        OnF = False


# Where you choose a class
def class_choice():
    choosing = True
    onWiz = True
    onWar = False
    too_little = False
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            while onWiz:
                screen.fill(white)
                screen.blit(MenuBack, [0, 0])
                file = open('name.pckl', 'rb')
                name = pickle.load(file)
                file.close()
                if len(name) == 0:
                    too_little = True
                    onWiz = False
                screen.blit(button, [-180, 227])
                screen.blit(button, [322, 227])
                message(60, 'The Adventures of ' + ''.join(name), green, NC, width / 2, 60)
                message(50, 'Choose a class', yellow, NC, width / 2, 120)
                message(55, 'Wizard', white, NC, width / 4, 500)
                message(30, 'Warrior', black, NC, width / 4 * 3, 500)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            onWar = True
                            onWiz = False
                        elif event.key == pygame.K_LEFT:
                            onWar = True
                            onWiz = False
                        elif event.key == pygame.K_RETURN:
                            wizGender()

            while onWar:
                screen.fill(white)
                screen.blit(MenuBack, [0, 0])
                file = open('name.pckl', 'rb')
                name = pickle.load(file)
                file.close()
                if len(name) == 0:
                    too_little = True
                    onWar = False
                screen.blit(button, [-180, 227])
                screen.blit(button, [322, 227])
                message(60, 'The Adventures of ' + ''.join(name), green, NC, width / 2, 60)
                message(50, 'Choose a class', yellow, NC, width / 2, 120)
                message(30, 'Wizard', black, NC, width / 4, 500)
                message(55, 'Warrior', white, NC, width / 4 * 3, 500)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            onWiz = True
                            onWar = False
                        elif event.key == pygame.K_RIGHT:
                            onWiz = True
                            onWar = False
                        elif event.key == pygame.K_RETURN:
                            warGender()
            while too_little:
                screen.fill(white)
                screen.blit(MenuBack, [0, 0])
                message(50, 'Please hit enter and then and enter a valid name', blue, NC, width / 2, height / 2)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            get_username()
                pygame.display.update()


# start up animation
def start_animate():
    startingUp = True
    direct = 'Up'
    titleHeight = 300
    while startingUp:
        screen.fill(white)
        screen.blit(MenuBack, [0, 0])
        pygame.display.update()
        if direct == 'Up':
            titleHeight -= 2
            if titleHeight == 0:
                startingUp = False

        screen.blit(gameTitle, [0, titleHeight])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update
        fpsClock.tick(FPS)


# Get the user name
def get_username():
    asking_u = True
    too_much = False
    name = []
    while too_much:
        screen.fill(white)
        screen.blit(MenuBack, [0, 0])
        message(40, 'Please enter less than 16 characters', yellow, NC, width / 2, height / 2)
        message(30, 'Press enter to return', red, NC, width / 2, height / 4 * 3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    asking_u = True
                    too_much = False

    while asking_u:
        screen.fill(white)
        screen.blit(MenuBack, [0, 0])
        file = open('name.pckl', 'wb')
        pickle.dump(name, file)
        file.close
        screen.blit(button, [73, 30])
        message(40, 'Please enter your name', white, NC, width / 2, height / 5)
        message(40, ''.join(name), black, NC, width / 2, height / 2)
        pygame.display.update()
        if len(name) > 16:
            too_much = True
            asking_u = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inMenu = True
                    asking_u = False
                elif event.key == pygame.K_SPACE:
                    name.append(' ')
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    class_choice()
                elif event.key == pygame.K_q:
                    name.append('q')
                elif event.key == pygame.K_w:
                    name.append('w')
                elif event.key == pygame.K_e:
                    name.append('e')
                elif event.key == pygame.K_r:
                    name.append('r')
                elif event.key == pygame.K_t:
                    name.append('t')
                elif event.key == pygame.K_y:
                    name.append('y')
                elif event.key == pygame.K_u:
                    name.append('u')
                elif event.key == pygame.K_i:
                    name.append('i')
                elif event.key == pygame.K_o:
                    name.append('o')
                elif event.key == pygame.K_p:
                    name.append('p')
                elif event.key == pygame.K_a:
                    name.append('a')
                elif event.key == pygame.K_s:
                    name.append('s')
                elif event.key == pygame.K_d:
                    name.append('d')
                elif event.key == pygame.K_f:
                    name.append('f')
                elif event.key == pygame.K_g:
                    name.append('g')
                elif event.key == pygame.K_h:
                    name.append('h')
                elif event.key == pygame.K_j:
                    name.append('j')
                elif event.key == pygame.K_k:
                    name.append('k')
                elif event.key == pygame.K_l:
                    name.append('l')
                elif event.key == pygame.K_z:
                    name.append('z')
                elif event.key == pygame.K_x:
                    name.append('x')
                elif event.key == pygame.K_c:
                    name.append('c')
                elif event.key == pygame.K_v:
                    name.append('v')
                elif event.key == pygame.K_b:
                    name.append('b')
                elif event.key == pygame.K_n:
                    name.append('n')
                elif event.key == pygame.K_m:
                    name.append('m')


# Menu Loop
def menu_loop():
    inMenu = True
    Play = True
    Quit = False
    # Play music
    pygame.mixer.music.play(loops=-1, start=0.0)
    while inMenu:
        # Add background to screen
        screen.fill(white)
        screen.blit(BackGround.image, BackGround.rect)
        # User input handling
        while Play:
            screen.fill(white)
            screen.blit(BackGround.image, BackGround.rect)
            message(60, 'The Adventures of <Insert Name Here>', yellow, NC, width / 2, 60)
            message(55, 'Play', white, NC, width / 2, 285)
            message(30, 'Quit', black, NC, width / 2, 510)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_RETURN:
                        get_username()
                    elif event.key == pygame.K_DOWN:
                        Quit = True
                        Play = False
                    elif event.key == pygame.K_UP:
                        Quit = True
                        Play = False
        while Quit:
            screen.fill(white)
            screen.blit(BackGround.image, BackGround.rect)
            message(60, 'The Adventures of <Insert Name Here>', yellow, NC, width / 2, 60)
            message(30, 'Play', black, NC, width / 2, 285)
            message(55, 'Quit', white, NC, width / 2, 510)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_UP:
                        Play = True
                        Quit = False
                    elif event.key == pygame.K_DOWN:
                        Play = True
                        Quit = False


# start_animate()
menu_loop()