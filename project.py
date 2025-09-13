import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))

pygame.display.set_caption("PROJECT")
clock= pygame.time.Clock()
test_font= pygame.font.Font('Elements/ByteBounce.ttf',50)
base_surface = pygame.image.load('Elements/Background.png')
resized_base = pygame.transform.scale(base_surface, (800, 400))
ground = pygame.image.load('Elements/ground.png')
resize_ground = pygame.transform.scale(ground,(800,32))
text_surface=test_font.render('MOB MECHA',False, 'Blue')
bot=pygame.image.load('Elements/Biker_run.png').convert_alpha()
resized_bot= pygame.transform.scale(bot,(244,60))
bot_position = 600









while True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(resized_base,(0,0))
    screen.blit(resize_ground,(0,390))
    screen.blit(text_surface,(300,30))
    bot_position+=4
    if bot_position>800: bot_position=-10
    screen.blit(resized_bot,(bot_position,330))

   






    


    pygame.display.update()
    clock.tick(40)
    


 