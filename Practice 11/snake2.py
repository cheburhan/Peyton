import pygame
from colors import * 
import random

# Инициализация Pygame
pygame.init()
pygame.font.init()

# --- ПАРАМЕТРЫ ОКНА ---
WIDTH = 450  
GAME_HEIGHT = 450 
UI_HEIGHT = 60    
HEIGHT = GAME_HEIGHT + UI_HEIGHT 
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Weights & Timers")

font = pygame.font.SysFont("Arial", 24)

def draw_grid():
    for i in range(GAME_HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (j * CELL, i * CELL + UI_HEIGHT, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(7, 7), Point(7, 8), Point(7, 9)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def check_wall_collision(self):
        head = self.body[0]
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= GAME_HEIGHT // CELL:
            return True
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def draw(self):
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL + UI_HEIGHT, CELL, CELL))

    def check_food_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            # Змейка растет. Добавляем сегмент в хвост
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            # Генерируем новую еду
            food.generate_random_pos(self.body)
            return True 
        return False

class Food:
    def __init__(self):
        self.pos = Point(5, 5)
        self.weight = 1
        self.timer = 0
        self.lifetime = 40 # Базовое время жизни еды (в тиках FPS)

    def draw(self):
        # Выбираем цвет в зависимости от веса
        if self.weight == 3:
            color = (0, 255, 255) # Голубой (очень ценный)
        elif self.weight == 2:
            color = (123, 123, 0) 
        else:
            color = colorGREEN    # Обычный
            
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL + UI_HEIGHT, CELL, CELL))
        
        # Визуальный таймер (маленькая полоска сверху еды)
        time_width = (self.timer / self.lifetime) * CELL
        pygame.draw.rect(screen, colorWHITE, (self.pos.x * CELL, self.pos.y * CELL + UI_HEIGHT, time_width, 3))

    def generate_random_pos(self, snake_body):
        while True:
            new_x = random.randint(0, (WIDTH // CELL) - 1)
            new_y = random.randint(0, (GAME_HEIGHT // CELL) - 1)
            collision = any(segment.x == new_x and segment.y == new_y for segment in snake_body)
            if not collision:
                self.pos.x = new_x
                self.pos.y = new_y
                # ЗАДАЧА: Случайный вес от 1 до 3
                self.weight = random.randint(1, 3)
                # ЗАДАЧА: Сброс таймера жизни (чем тяжелее еда, тем меньше она живет)
                self.timer = self.lifetime - (self.weight * 5)
                break

    def update(self, snake_body):
        # ЗАДАЧА: Уменьшение таймера
        self.timer -= 1
        if self.timer <= 0:
            self.generate_random_pos(snake_body)

# Настройки игры
FPS = 5  
score = 0
level = 1
foods_to_next_level = 3 
collected_on_current_level = 0

clock = pygame.time.Clock()
food = Food()
snake = Snake()
food.generate_random_pos(snake.body)

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1

    screen.fill(colorBLACK)
    
    # UI панель
    pygame.draw.rect(screen, (40, 40, 40), (0, 0, WIDTH, UI_HEIGHT))
    pygame.draw.line(screen, colorWHITE, (0, UI_HEIGHT), (WIDTH, UI_HEIGHT), 2)
    
    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (20, UI_HEIGHT // 4))
    screen.blit(level_text, (WIDTH - 120, UI_HEIGHT // 4))

    draw_grid()

    if not game_over:
        snake.move()
        # Обновляем таймер еды
        food.update(snake.body)
        
        if snake.check_wall_collision():
            game_over = True
            
        if snake.check_food_collision(food):
            # Добавляем очки согласно весу еды
            score += 10 * food.weight 
            collected_on_current_level += 1
            
            # Повышение уровня
            if collected_on_current_level >= foods_to_next_level:
                level += 1
                FPS += 1
                collected_on_current_level = 0

    snake.draw()
    if not game_over:   
        food.draw()

    if game_over:
        game_over_text = font.render("GAME OVER", True, colorRED)
        text_rect = game_over_text.get_rect(center=(WIDTH/2, (GAME_HEIGHT/2) + UI_HEIGHT))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()