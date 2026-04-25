import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
ball = Ball(WIDTH // 2, HEIGHT // 2, radius=25, color=RED, speed=20)

font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move_up(HEIGHT)
            elif event.key == pygame.K_DOWN:
                ball.move_down(HEIGHT)
            elif event.key == pygame.K_LEFT:
                ball.move_left(WIDTH)
            elif event.key == pygame.K_RIGHT:
                ball.move_right(WIDTH)
    
 
    screen.fill(WHITE) 
    ball.draw(screen)
    

    instruction_text = font.render("Use Arrow Keys to Move", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - 150, 20))
    
    pos_x, pos_y = ball.get_position()
    pos_text = font.render(f"Position: ({pos_x}, {pos_y})", True, BLACK)
    screen.blit(pos_text, (20, HEIGHT - 40))
    pygame.display.flip()
    clock.tick(60)

# Выход
pygame.quit()