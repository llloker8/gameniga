import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Cubes Game')

walkRight = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png'), pygame.image.load('right_3.png'), pygame.image.load('right_4.png'), pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'), pygame.image.load('left_3.png'), pygame.image.load('left_4.png'), pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]

bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('idle.png')

clock = pygame.time.Clock()

x = 50
y = 450
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1

    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    pygame.display.update()
run = True


while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x-= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1280 - width - 5:
        x+= speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    class Menu:
        def __init__(self, punkts = [120, 140, u'Punkt', (250,250,30), (250,30,250)]):
            self.punkts = punkts
        def render(self, poverhnost, font, num_punkt):
            for i in self.punkts:
                if num_punkt == i[5]:
                    poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
                else:
                    poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))


    drawWindow()
pygame.quit()
