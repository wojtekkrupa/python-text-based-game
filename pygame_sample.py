from time import sleep
import pygame
import pygcurse

win = pygcurse.PygcurseWindow(80, 40)
print(pygame.font.get_fonts())
win.font = pygame.font.SysFont('consolas', 12)

win.write('What is your name?')
name = win.input("so... who are you eh? > ")

win.write('Hello, ')
win.fgcolor = 'red'
win.write(name + '!\n')
win.colors = ('red', 'green')

# printing with pygprint -additional end, as in regular print function
# for char in 'It is good to meet you!':
#     sleep(0.1)
#     win.pygprint('What is your name?', end='')
#     win.pygprint('')

#printing with win.write
# for char in 'It is good to meet you!':
#     sleep(0.1)
#     win.write(char)

for char in f'It is good to meet you, {name}!':
    sleep(0.05)
    win.write(char)
win.write("\n")

greeting= f'It is good to meet you, {name}!'
for i, char in enumerate(greeting):
    sleep(0.05)
    win.write(char, x=7+i, y=10,
              fgcolor=pygame.color.THECOLORS['burlywood1'],
              bgcolor=pygame.color.THECOLORS['bisque'])
win.write("\n")


for char in 'It is good to meet you!':
    sleep(0.05)
    win.write(char)
win.write("\n")

pygcurse.waitforkeypress()

FPS = 25
WINDOWWIDTH = 26
WINDOWHEIGHT = 27
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = None

LEFTMARGIN = 4
TOPMARGIN = 4

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.15
print(pygame.color.THECOLORS.keys())

WINDOWSURF = pygcurse.PygcurseWindow(80, 30, 'Textris', font=pygame.font.Font(None, 12))
WINDOWSURF.autoupdate = False
BOARDBOX = pygcurse.PygcurseTextbox(WINDOWSURF,
                                    (LEFTMARGIN - 1, TOPMARGIN - 1, 10, 10),
                                    border="rouded",
                                    bgcolor=pygame.color.THECOLORS['springgreen4'])
BOARDBOX.update()

pygcurse.waitforkeypress()