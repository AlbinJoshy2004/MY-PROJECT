import pygame
from rider_ import RiderIdle
from rider_move import RiderMove

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("PROJECT")
clock = pygame.time.Clock()

test_font = pygame.font.Font("python/Elements/ByteBounce.ttf", 50)
base_surface = pygame.image.load("python/Elements/Background.png")
resized_base = pygame.transform.scale(base_surface, (800, 400))
ground = pygame.image.load("python/Elements/ground.png").convert()
resize_ground = pygame.transform.scale(ground, (800, 200))
text_surface = test_font.render('MOB MECHA', False, 'Blue')

rider = RiderIdle(100, 300)
all_sprites = pygame.sprite.Group(rider)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # ✅ Sprite switching logic (outside of event loop)
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        if not isinstance(rider, RiderMove):
            rider = RiderMove(rider.rect.x, rider.rect.y)
            all_sprites.empty()
            all_sprites.add(rider)
    else:
        if not isinstance(rider, RiderIdle):
            rider = RiderIdle(rider.rect.x, rider.rect.y)
            all_sprites.empty()
            all_sprites.add(rider)

    # ✅ Drawing
    screen.blit(resized_base, (0, 0))
    screen.blit(resize_ground, (0, 390))
    screen.blit(text_surface, (300, 30))

    # ✅ Update sprites (with key input)
    all_sprites.update(keys)
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(40)
