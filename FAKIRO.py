import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption('Fakiro')

WIDTH = 800
HEIGHT = 600
player_velocity = 5
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for x in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(x * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "") = sprites

    return all_sprites

class Player(pygame.sprite.Sprite):
    color = (0, 0, 255)
    gravity = 1
    SPRITES = load_sprite_sheets(, , 32, 32, True)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
                self.direction = "left"
                self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.gravity)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1
        

    def draw(self, win):
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))

def get_Background(name):
    image = pygame.image.load("assets/background/Blue.png")
    _, _, width, height = image.get_rect()
    tiles = []

    for w in range(WIDTH // width + 1):
        for h in range(HEIGHT // height + 1):
            pos = (w*width, h*height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)
    
    pygame.display.update()


def move_Player(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_left(player_velocity)
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_right(player_velocity)
    

def load_Game(window):
    clock = pygame.time.Clock()
    background, bg_image = get_Background("Blue.png")

    player = Player(100, 100, 50, 50)
    
    run = True
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        move_Player(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    load_Game(window)
