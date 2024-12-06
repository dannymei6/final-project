import pygame

pygame.init()

pygame.display.set_caption('Fakiro')

WIDTH = 800
HEIGHT = 600
player_velocity = 5
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_Background(name):
    image = pygame.image.load("assets/background/Blue.png")
    _, _, width, height = image.get_rect()
    tiles = []

    for w in range(WIDTH // width + 1):
        for h in range(HEIGHT // height + 1):
            pos = (w*width, h*height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)
    
    pygame.display.update()


def loadGame(window):
    clock = pygame.time.Clock()
    background, bg_image = get_Background("Blue.png")
    
    run = True
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)

    pygame.quit()
    quit()
    

if __name__ == "__main__":
    loadGame(window)
