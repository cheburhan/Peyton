import pygame # type: ignore
import random
import time

pygame.init() 

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game - Simple Hitbox")

# --- Загрузка и подготовка ресурсов ---
def load_img(path, size):
    try:
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, size)
    except:
        surf = pygame.Surface(size); surf.fill((200, 0, 0))
        return surf

# Подгоняем размеры машин под экран
image_background = load_img('doroja.jpeg', (WIDTH, HEIGHT))
image_player = load_img('redcar.png', (55, 110)) # Чуть меньше для маневренности
image_enemy = load_img('greencar.png', (55, 110))

image_coin = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.circle(image_coin, (255, 215, 0), (15, 15), 15)

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# Глобальные переменные
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
bg_y = 0

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 10000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 8

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.centerx = random.randint(50, WIDTH - 50)
        self.rect.bottom = random.randint(-500, -150)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            SCORE += 1
            self.spawn()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.centerx = random.randint(30, WIDTH - 30)
        self.rect.bottom = random.randint(-400, -50)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.spawn()

# Инициализация
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INC_SPEED:
            SPEED += 0.5

    P1.move()
    for entity in all_sprites:
        if entity != P1:
            entity.move()

    # --- Прямоугольная проверка коллизий ---
    
    # Коллизия с монетой (используем стандартный rect)
    if P1.rect.colliderect(C1.rect):
        COINS_COLLECTED += 1
        C1.spawn()

    
    if P1.rect.inflate(-15, -30).colliderect(E1.rect.inflate(-15, -30)):
        screen.fill("red")
        game_over_txt = font_big.render("GAME OVER", True, "black")
        screen.blit(game_over_txt, game_over_txt.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        time.sleep(2)
        running = False

    # Отрисовка
    screen.blit(image_background, (0, bg_y))
    screen.blit(image_background, (0, bg_y - HEIGHT))
    bg_y += SPEED
    if bg_y >= HEIGHT: bg_y = 0

    score_lbl = font_small.render(f"Score: {SCORE}", True, "black")
    coin_lbl = font_small.render(f"Coins: {COINS_COLLECTED}", True, "black")
    screen.blit(score_lbl, (10, 10))
    screen.blit(coin_lbl, (WIDTH - 130, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()