import pygame
import random

# Запуск Pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 800, 600
WHITE = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра Тир")

# Параметры игры
target_radius = 20
score = 0
font = pygame.font.SysFont(None, 36)

# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Проверка попадания в мишень
            if (random_x - mouse_x) ** 2 + (random_y - mouse_y) ** 2 < target_radius ** 2:
                score += 1

    # Заполнение экрана выбранным цветом
    screen.fill(WHITE)

    # Отображение мишени
    random_x = random.randint(target_radius, WIDTH - target_radius)
    random_y = random.randint(target_radius, HEIGHT - target_radius)
    pygame.draw.circle(screen, RED, (random_x, random_y), target_radius)

    # Отображение счета
    draw_text(f"Счет: {score}", font, BLACK, screen, 10, 10)

    # Обновление экрана
    pygame.display.flip()

    # Время смены положения мишени
    pygame.time.delay(1300)

# Завершение Pygame
pygame.quit()
