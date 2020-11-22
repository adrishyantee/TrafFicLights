import pygame
pygame.init()
SIDE=500
win = pygame.display.set_mode((400, 590))
pygame.display.set_caption("TRAFFIC LIGHT")
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

red_visible = False
green_visible = False
yellow_visible = False
reset = False

FONT = pygame.font.SysFont('Times New Roman', 20)
clock = pygame.time.Clock()
run = True

images = []
for i in range(1, 5):
    image = pygame.image.load("C:/Users/adris/OneDrive/Desktop/PycharmProjects/FirstProj/bg"+str(i)+".jpg")
    images.append(image)


def drawwindow():
    win.blit(images[0], (0, 0))

    if red_visible:
        win.blit(images[1], (0, 0))
        text = FONT.render("STOP!", True, red)
        win.blit(text, (SIDE / 2 - (text.get_width()/2+40), 500))
    if yellow_visible:
        win.blit(images[2], (0, 0))
        text = FONT.render("PREPARE...", True, black)
        win.blit(text, (SIDE / 2 - (text.get_width()/2+40), 500))
    if green_visible:
        win.blit(images[3], (0, 0))
        text = FONT.render("LETS GO!", True, green)
        win.blit(text, (SIDE / 2 - (text.get_width()/2+40), 500))
    if reset:
        win.blit(images[0], (0, 0))
        text = FONT.render("All Lights RESET !", True, black)
        win.blit(text, (SIDE / 2 - (text.get_width()/2+40), 500))

    text = FONT.render("TRAFFIC LIGHT - Adrishyantee Maiti", True, black)
    win.blit(text, (SIDE / 2 - (text.get_width()/2+40), 520))

    pygame.display.update()


while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                red_visible = True
                green_visible = False
                yellow_visible = False
                reset = False
            if event.key == pygame.K_s:
                yellow_visible = True
                green_visible = False
                red_visible = False
                reset = False
            if event.key == pygame.K_d:
                yellow_visible = False
                green_visible = True
                red_visible = False
                reset = False
            if event.key == pygame.K_w:
                yellow_visible = False
                green_visible = False
                red_visible = False
                reset = True

    drawwindow()
pygame.quit()