import pygame

pygame.init()

pygame.display.set_caption('Fakiro')

WIDTH = 800
HEIGHT = 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))


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

    pygame.quit()
    quit()


if __name__ == "__main__":
    loadGame(window)