import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pygame Paint Tool - Extended")
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    tool = 'line'  
    
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0)) 
    
    drawing = False
    start_pos = None
    last_pos = None

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return
            
                # Выбор цвета
                if event.key == pygame.K_1: mode = 'red'
                elif event.key == pygame.K_2: mode = 'green'
                elif event.key == pygame.K_3: mode = 'blue'
                
                # Выбор инструментов (старые + новые)
                elif event.key == pygame.K_l: tool = 'line'
                elif event.key == pygame.K_r: tool = 'rect'
                elif event.key == pygame.K_c: tool = 'circle'
                elif event.key == pygame.K_e: tool = 'eraser'
                elif event.key == pygame.K_s: tool = 'square'    # Квадрат
                elif event.key == pygame.K_t: tool = 'right_tr' # Прямоугольный 
                elif event.key == pygame.K_u: tool = 'equil_tr' # Равносторонний 
                elif event.key == pygame.K_h: tool = 'rhombus'  # Ромб
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                elif event.button == 3: 
                    radius = max(1, radius - 1)
                elif event.button == 2: 
                    radius = min(200, radius + 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    # Фигуры, которые рисуются перетаскиванием
                    if tool in ['rect', 'circle', 'square', 'right_tr', 'equil_tr', 'rhombus']:
                        draw_shape(canvas, tool, start_pos, event.pos, mode, radius)

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'line':
                        draw_line(canvas, last_pos, event.pos, mode, radius)
                    elif tool == 'eraser':
                        draw_line(canvas, last_pos, event.pos, 'black', radius)
                    last_pos = event.pos
                    
        screen.blit(canvas, (0, 0))
        
        # Предпросмотр для всех фигур
        if drawing and tool not in ['line', 'eraser']:
            current_pos = pygame.mouse.get_pos()
            draw_shape(screen, tool, start_pos, current_pos, mode, radius)

        pygame.display.flip()
        clock.tick(60)

def get_color(mode):
    if mode == 'red': return (255, 0, 0)
    if mode == 'green': return (0, 255, 0)
    if mode == 'blue': return (0, 0, 255)
    if mode == 'black': return (0, 0, 0)
    return (255, 255, 255)

def draw_shape(surface, tool, start, end, mode, width):
    color = get_color(mode)
    x1, y1 = start
    x2, y2 = end
    
    if tool == 'rect':
        rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
        rect.normalize()
        pygame.draw.rect(surface, color, rect, width if width < min(rect.width//2, rect.height//2) else 0)
        
    elif tool == 'square':
        # Квадрат: берем минимальную разницу координат, чтобы стороны были равны
        side = max(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, side if x2 > x1 else -side, side if y2 > y1 else -side)
        rect.normalize()
        pygame.draw.rect(surface, color, rect, width if width < side//2 else 0)

    elif tool == 'circle':
        circ_radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(surface, color, start, circ_radius, width if width < circ_radius else 0)

    elif tool == 'right_tr':
        # Прямоугольный треугольник (катеты параллельны осям)
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(surface, color, points, width)

    elif tool == 'equil_tr':
        # Равносторонний треугольник
        height = (y2 - y1)
        side = 2 * height / math.sqrt(3)
        points = [(x1, y1), (x1 - side//2, y2), (x1 + side//2, y2)]
        pygame.draw.polygon(surface, color, points, width)

    elif tool == 'rhombus':
        # Ромб (вершины на серединах сторон воображаемого прямоугольника)
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
        pygame.draw.polygon(surface, color, points, width)

def draw_line(surface, start, end, mode, width):
    color = get_color(mode)
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations + 1):
        progress = i / iterations if iterations != 0 else 0
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

if __name__ == "__main__":
    main()