import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing_rect = False
    drawing_circle = False
    eraser = False
    color = (0, 0, 255)
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    eraser = not eraser
                elif event.key == pygame.K_c:
                    color = (255, 255, 255)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing_rect = True
                    start_pos = event.pos
                elif event.button == 3:
                    drawing_circle = True
                    start_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing_rect = False
                    end_pos = event.pos
                    pygame.draw.rect(screen, color, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
                elif event.button == 3:
                    drawing_circle = False
                    end_pos = event.pos
                    radius = max(1, int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5))
                    pygame.draw.circle(screen, color, start_pos, radius)
            
            if event.type == pygame.MOUSEMOTION:
                if not drawing_rect and not drawing_circle:
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, eraser)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, eraser):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if not eraser:
            pygame.draw.circle(screen, color, (x, y), width)
        else:
            pygame.draw.circle(screen, (255, 255, 255), (x, y), width)

main()
