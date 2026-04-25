import pygame
import random
import time

pygame.init() 

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game - Coins Weights")

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
image_player = load_img('redcar.png', (55, 110)) 
image_enemy = load_img('greencar.png', (55, 110))

# Функция для создания картинки монеты разного размера в зависимости от веса
def get_coin_surface(weight):
    # Чем тяжелее монета, тем она больше визуально
    size = 20 + (weight * 5) 
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(surf, (255, 215, 0), (size // 2, size // 2), size // 2)
    return surf

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# Глобальные переменные
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
COINS_TO_SPEED_UP = 5 # Ускоряем врага каждые 10 собранных монет (N)
bg_y = 0

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
        self.weight = 1 # Вес монеты по умолчанию
        self.spawn()

    def spawn(self):
        # Генерируем случайный вес от 1 до 3
        self.weight = random.randint(1, 5)
        # Обновляем изображение в зависимости от веса
        self.image = get_coin_surface(self.weight)
        self.rect = self.image.get_rect()
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

    P1.move()
    for entity in all_sprites:
        if entity != P1:
            entity.move()

    # --- Коллизия с монетой ---
    if P1.rect.colliderect(C1.rect):
        old_coins = COINS_COLLECTED
        COINS_COLLECTED += C1.weight # Добавляем вес монеты к общему счету
        
        # если порог монет пройден, увеличиваем скорость
        if (COINS_COLLECTED // COINS_TO_SPEED_UP) > (old_coins // COINS_TO_SPEED_UP):
            SPEED += 1 
            
        C1.spawn()

    # --- Коллизия с врагом ---
    if P1.rect.inflate(-15, -30).colliderect(E1.rect.inflate(-15, -30)):
        screen.fill("red")
        game_over_txt = font_big.render("GAME OVER", True, "black")
        screen.blit(game_over_txt, game_over_txt.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        time.sleep(2)
        running = False

    # Отрисовка фона
    screen.blit(image_background, (0, bg_y))
    screen.blit(image_background, (0, bg_y - HEIGHT))
    bg_y += SPEED
    if bg_y >= HEIGHT: bg_y = 0

    # Интерфейс
    score_lbl = font_small.render(f"Score: {SCORE}", True, "black")
    coin_lbl = font_small.render(f"Coins: {COINS_COLLECTED}", True, "black")
    speed_lbl = font_small.render(f"Speed: {SPEED}", True, "black")
    
    screen.blit(score_lbl, (10, 10))
    screen.blit(coin_lbl, (WIDTH - 130, 10))
    screen.blit(speed_lbl, (10, 40))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()