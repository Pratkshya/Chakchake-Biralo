import pygame

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Chakchake Biralo")

clock = pygame.time.Clock()

biralo = pygame.image.load("cat.png").convert_alpha() #maintains transparency
resized_biralo = pygame.transform.smoothscale(biralo, (100, 100))
img = resized_biralo.get_rect()
run = True      
while run:

    clock.tick(60) #controls frame rate
    screen.fill((255,250,250))

    screen.blit(resized_biralo, img)

    #move the image
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        img.move_ip(-5,0)
    elif key[pygame.K_d] == True:
        img.move_ip(5,0)
    elif key[pygame.K_w] == True:
        img.move_ip(0,-5)
    elif key[pygame.K_s] == True:
        img.move_ip(0,5) 

    #check for quit event
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            run = False

    pygame.display.flip()        

pygame.quit()

