import random, sys, time, math, pygame
from pygame.locals import *

FPS = 30

#Rozmiary okienka

WIN_WIDTH = 940
WIN_HEIGHT = 680
HALF_WIN_WIDTH = int(WIN_WIDTH / 2)
HALF_WIN_HEIGHT = int(WIN_HEIGHT / 2)


#Kolory
GRASS_COLOR = (24, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (76,76,255)


CAMERASLACK = 90
MOVERATE = 9
BOUNCERATE = 6
BOUNCEHEIGHT = 30
STARTSIZE = 25
WINSIZE = 300
INVULNTIME = 2
GAMEOVERTIME = 11
NUMGRASS = 160

#Poziom trudności
MAXHEALTH = 3
NUM_ICE_CREAMS = 70
BOY_MIN_SPEED = 3
BOY_MAX_SPEED = 7
DIRCHANGEFREQ = 2

LEFT = 'left'
RIGHT = 'right'


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_BOY_IMG, R_BOY_IMG, GRASSIMAGES, ICE_CREAM, LOLLIPOP
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('FatBoy.png'))
    DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Fat Boy Dreams v. 1.1 (With  NEW Sounds!)')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    LOLLIPOP = pygame.image.load('lolipop.png')
    ICE_CREAM = pygame.image.load('iceCream.png')
    L_BOY_IMG = pygame.image.load('FatBoy.png')
    R_BOY_IMG = pygame.transform.flip(L_BOY_IMG, True, False)
    GRASSIMAGES = []
    for i in range(1, 5):
        GRASSIMAGES.append(pygame.image.load('grass%s.png' % i))

    while True:
        runGame()

def runGame():
    pygame.mixer.music.load("Mika.mp3")
    pygame.mixer.music.play(1, 0.0)
    global gameOverMode

    invulnerableMode = False
    invulnerableStartTime = 0
    gameOverMode = False
    gameOverStartTime = 0
    winMode = False


    gameOverSurf = BASICFONT.render('Ice Creams Eats You...', True, RED)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (HALF_WIN_WIDTH, HALF_WIN_HEIGHT)

    winSurf = BASICFONT.render('You Are Really Really Fat Boy !', True, WHITE)
    winRect = winSurf.get_rect()
    winRect.center = (HALF_WIN_WIDTH, HALF_WIN_HEIGHT)

    winSurf2 = BASICFONT.render('(Press "R" to restart.)', True, WHITE)
    winRect2 = winSurf2.get_rect()
    winRect2.center = (HALF_WIN_WIDTH, HALF_WIN_HEIGHT + 30)

    camerax = 0
    cameray = 0
    grassObjs = []
    squirrelObjs = []

    playerObj = {'surface': pygame.transform.scale(L_BOY_IMG, (STARTSIZE, STARTSIZE)),
                 'facing': LEFT,
                 'size': STARTSIZE,
                 'x': HALF_WIN_WIDTH,
                 'y': HALF_WIN_HEIGHT,
                 'bounce': 0,
                 'health': MAXHEALTH}

    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False


    for i in range(10):
        grassObjs.append(makeNewGrass(camerax, cameray))
        grassObjs[i]['x'] = random.randint(0, WIN_WIDTH)
        grassObjs[i]['y'] = random.randint(0, WIN_HEIGHT)

    while True:

        if invulnerableMode and time.time() - invulnerableStartTime > INVULNTIME:
            invulnerableMode = False


        for sObj in squirrelObjs:

            sObj['x'] += sObj['movex']
            sObj['y'] += sObj['movey']
            sObj['bounce'] += 1
            if sObj['bounce'] > sObj['bouncerate']:
                sObj['bounce'] = 0


            if random.randint(0, 99) < DIRCHANGEFREQ:
                sObj['movex'] = getRandomVelocity()
                sObj['movey'] = getRandomVelocity()
                if sObj['movex'] > 0:
                    sObj['surface'] = pygame.transform.scale(ICE_CREAM, (sObj['width'], sObj['height']))
                else:  # faces left
                    sObj['surface'] = pygame.transform.scale(ICE_CREAM, (sObj['width'], sObj['height']))


        for i in range(len(grassObjs) - 1, -1, -1):
            if isOutsideActiveArea(camerax, cameray, grassObjs[i]):
                del grassObjs[i]
        for i in range(len(squirrelObjs) - 1, -1, -1):
            if isOutsideActiveArea(camerax, cameray, squirrelObjs[i]):
                del squirrelObjs[i]


        while len(grassObjs) < NUMGRASS:
            grassObjs.append(makeNewGrass(camerax, cameray))
        while len(squirrelObjs) < NUM_ICE_CREAMS:
            squirrelObjs.append(makeNewIceCream(camerax, cameray))



        playerCenterx = playerObj['x'] + int(playerObj['size'] / 2)
        playerCentery = playerObj['y'] + int(playerObj['size'] / 2)
        if (camerax + HALF_WIN_WIDTH) - playerCenterx > CAMERASLACK:
            camerax = playerCenterx + CAMERASLACK - HALF_WIN_WIDTH
        elif playerCenterx - (camerax + HALF_WIN_WIDTH) > CAMERASLACK:
            camerax = playerCenterx - CAMERASLACK - HALF_WIN_WIDTH
        if (cameray + HALF_WIN_HEIGHT) - playerCentery > CAMERASLACK:
            cameray = playerCentery + CAMERASLACK - HALF_WIN_HEIGHT
        elif playerCentery - (cameray + HALF_WIN_HEIGHT) > CAMERASLACK:
            cameray = playerCentery - CAMERASLACK - HALF_WIN_HEIGHT


        DISPLAYSURF.fill(GRASS_COLOR)

        for gObj in grassObjs:
            gRect = pygame.Rect((gObj['x'] - camerax,
                                 gObj['y'] - cameray,
                                 gObj['width'],
                                 gObj['height']))
            DISPLAYSURF.blit(GRASSIMAGES[gObj['grassImage']], gRect)


        for sObj in squirrelObjs:
            sObj['rect'] = pygame.Rect((sObj['x'] - camerax,
                                        sObj['y'] - cameray - getBounceAmount(sObj['bounce'], sObj['bouncerate'],
                                                                              sObj['bounceheight']),
                                        sObj['width'],
                                        sObj['height']))
            DISPLAYSURF.blit(sObj['surface'], sObj['rect'])


        flashIsOn = round(time.time(), 1) * 10 % 2 == 1
        if not gameOverMode and not (invulnerableMode and flashIsOn):
            playerObj['rect'] = pygame.Rect((playerObj['x'] - camerax,
                                             playerObj['y']
                                             - cameray - getBounceAmount(playerObj['bounce'], BOUNCERATE, BOUNCEHEIGHT),
                                            playerObj['size'],
                                            playerObj['size']) )
            DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])


        drawHealthMeter(playerObj['health'])

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    moveDown = False
                    moveUp = True
                elif event.key in (K_DOWN, K_s):
                    moveUp = False
                    moveDown = True
                elif event.key in (K_LEFT, K_a):
                    moveRight = False
                    moveLeft = True
                    if playerObj['facing'] == RIGHT:
                        playerObj['surface'] = pygame.transform.scale(L_BOY_IMG,
                                                                      (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = LEFT
                elif event.key in (K_RIGHT, K_d):
                    moveLeft = False
                    moveRight = True
                    if playerObj['facing'] == LEFT:
                        playerObj['surface'] = pygame.transform.scale(R_BOY_IMG,
                                                                      (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = RIGHT
                elif winMode and event.key == K_r:
                    return

            elif event.type == KEYUP:

                if event.key in (K_LEFT, K_a):
                    moveLeft = False
                elif event.key in (K_RIGHT, K_d):
                    moveRight = False
                elif event.key in (K_UP, K_w):
                    moveUp = False
                elif event.key in (K_DOWN, K_s):
                    moveDown = False

                elif event.key == K_ESCAPE:
                    terminate()

        if not gameOverMode:
            # Ruch gracza
            if moveLeft:
                playerObj['x'] -= MOVERATE
            if moveRight:
                playerObj['x'] += MOVERATE
            if moveUp:
                playerObj['y'] -= MOVERATE
            if moveDown:
                playerObj['y'] += MOVERATE

            if (moveLeft or moveRight or moveUp or moveDown) or playerObj['bounce'] != 0:
                playerObj['bounce'] += 1

            if playerObj['bounce'] > BOUNCERATE:
                playerObj['bounce'] = 0


            for i in range(len(squirrelObjs) - 1, -1, -1):
                sqObj = squirrelObjs[i]
                if 'rect' in sqObj and playerObj['rect'].colliderect(sqObj['rect']):
                    # Kolizja gracz -> lód

                    if sqObj['width'] * sqObj['height'] <= playerObj['size'] ** 2:
                        # Zjada lody
                        playerObj['size'] += int((sqObj['width'] * sqObj['height']) ** 0.2) + 1
                        del squirrelObjs[i]

                        if playerObj['facing'] == LEFT:
                            playerObj['surface'] = pygame.transform.scale(L_BOY_IMG,
                                                                          (playerObj['size'], playerObj['size']))
                        if playerObj['facing'] == RIGHT:
                            playerObj['surface'] = pygame.transform.scale(R_BOY_IMG,
                                                                          (playerObj['size'], playerObj['size']))

                        if playerObj['size'] > WINSIZE:
                            winMode = True  # Odpala tryb wygranej


                    elif not invulnerableMode:
                        # Obrazenia kiedy gracz jest mmiejszy
                        invulnerableMode = True
                        invulnerableStartTime = time.time()
                        playerObj['health'] -= 1
                        if playerObj['health'] == 0:
                            pygame.mixer.music.load("Darkness.mp3")
                            pygame.mixer.music.play(0, 0.0)
                            gameOverMode = True  # turn on "game over mode"
                            gameOverStartTime = time.time()
        else:

            # "GAME OVER" na ekranie
            DISPLAYSURF.blit(gameOverSurf, gameOverRect)
            if time.time() - gameOverStartTime > GAMEOVERTIME:
                pygame.mixer.music.stop()

                return

        # Czy Wygrana?
        if winMode:
            DISPLAYSURF.blit(winSurf, winRect)
            DISPLAYSURF.blit(winSurf2, winRect2)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawHealthMeter(currentHealth):
    for i in range(currentHealth):
        pygame.draw.rect(DISPLAYSURF, RED, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10))
    for i in range(MAXHEALTH):
        pygame.draw.rect(DISPLAYSURF, WHITE, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10), 1)


def terminate():
    pygame.quit()
    sys.exit()


def getBounceAmount(currentBounce, bounceRate, bounceHeight):
    return int(math.sin((math.pi / float(bounceRate)) * currentBounce) * bounceHeight)


def getRandomVelocity():
    speed = random.randint(BOY_MIN_SPEED, BOY_MAX_SPEED)
    if random.randint(0, 1) == 0:
        return speed
    else:
        return -speed


def getRandomOffCameraPos(camerax, cameray, objWidth, objHeight):

    cameraRect = pygame.Rect(camerax, cameray, WIN_WIDTH, WIN_HEIGHT)
    while True:
        x = random.randint(camerax - WIN_WIDTH, camerax + (2 * WIN_WIDTH))
        y = random.randint(cameray - WIN_HEIGHT, cameray + (2 * WIN_HEIGHT))


        objRect = pygame.Rect(x, y, objWidth, objHeight)
        if not objRect.colliderect(cameraRect):
            return x, y


def makeNewIceCream(camerax, cameray):
    sq = {}
    generalSize = random.randint(5, 25)
    multiplier = random.randint(1, 3)
    sq['width'] = (generalSize + random.randint(0, 10)) * multiplier
    sq['height'] = (generalSize + random.randint(0, 10)) * multiplier
    sq['x'], sq['y'] = getRandomOffCameraPos(camerax, cameray, sq['width'], sq['height'])
    sq['movex'] = getRandomVelocity()
    sq['movey'] = getRandomVelocity()
    if sq['movex'] < 0:
        sq['surface'] = pygame.transform.scale(ICE_CREAM, (sq['width'], sq['height']))
    else:
        sq['surface'] = pygame.transform.scale(ICE_CREAM, (sq['width'], sq['height']))
    sq['bounce'] = 0
    sq['bouncerate'] = random.randint(10, 18)
    sq['bounceheight'] = random.randint(10, 50)
    return sq



def makeNewGrass(camerax, cameray):
    gr = {}
    gr['grassImage'] = random.randint(0, len(GRASSIMAGES) - 1)
    gr['width'] = GRASSIMAGES[0].get_width()
    gr['height'] = GRASSIMAGES[0].get_height()
    gr['x'], gr['y'] = getRandomOffCameraPos(camerax, cameray, gr['width'], gr['height'])
    gr['rect'] = pygame.Rect((gr['x'], gr['y'], gr['width'], gr['height']))
    return gr


def isOutsideActiveArea(camerax, cameray, obj):
    boundsLeftEdge = camerax - WIN_WIDTH
    boundsTopEdge = cameray - WIN_HEIGHT
    boundsRect = pygame.Rect(boundsLeftEdge, boundsTopEdge, WIN_WIDTH * 3, WIN_HEIGHT * 3)
    objRect = pygame.Rect(obj['x'], obj['y'], obj['width'], obj['height'])
    return not boundsRect.colliderect(objRect)


if __name__ == '__main__':
    main()