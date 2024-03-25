import pygame
import sys

pygame.init()

# Definisikan warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Inisialisasi layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformasi 2D")

objects = []


class Object:
    def __init__(self, shape, color, position):
        self.shape = shape
        self.color = color
        self.position = position

    def draw(self):
        if self.shape == "square":
            pygame.draw.rect(screen, self.color, self.position)
        elif self.shape == "circle":
            pygame.draw.circle(screen, self.color, self.position, 50)
        elif self.shape == "triangle":
            pygame.draw.polygon(screen, self.color, self.position)


def main():
    running = True
    selected_object = None
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    objects.append(Object("circle", RED, pos))
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_object = None
        for obj in objects:
            obj.draw()
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
