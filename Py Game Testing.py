import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

screenWidth = 500
screenHeight = 500

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_d] and x < screenWidth - width - vel:
        x += vel
    if keys[pygame.K_w] and y > vel:
        y -= vel
    if keys[pygame.K_s] and y < screenHeight - height - vel:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()