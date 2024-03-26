import pygame
import sys

pygame.init()

# Definisi warna

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Inisialisasi layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(
    "Press 'r' / 'c' / 't' to create shapes | Drag to move the shapes")


class Shape:
    def __init__(self, shape, color, rect):
        self.shape = shape
        self.color = color
        self.rect = rect

    def draw(self):
        if self.shape == "rectangle":
            pygame.draw.rect(screen, self.color, self.rect)
        elif self.shape == "circle":
            pygame.draw.circle(screen, self.color,
                               self.rect.center, self.rect.width // 2)
        elif self.shape == "triangle":
            points = [(self.rect.left, self.rect.bottom), ((
                self.rect.left + self.rect.right) // 2, self.rect.top), (self.rect.right, self.rect.bottom)]
            pygame.draw.polygon(screen, self.color, points)


def main():
    shapes = []
    dragging = False
    selected_shape = None
    offset = [0, 0]

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Mouse left button
                    pos = pygame.mouse.get_pos()
                    for shape in reversed(shapes):
                        if shape.rect.collidepoint(pos):
                            selected_shape = shape
                            dragging = True
                            offset[0] = shape.rect.x - pos[0]
                            offset[1] = shape.rect.y - pos[1]
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Mouse left button
                    dragging = False
                    selected_shape = None

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    pos = pygame.mouse.get_pos()
                    selected_shape.rect.x = pos[0] + offset[0]
                    selected_shape.rect.y = pos[1] + offset[1]

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press 'r' to create a rectangle
                    rect = pygame.Rect(100, 100, 100, 50)
                    shapes.append(Shape("rectangle", BLACK, rect))
                elif event.key == pygame.K_c:  # Press 'c' to create a circle
                    circle = pygame.Rect(200, 200, 100, 100)
                    shapes.append(Shape("circle", RED, circle))
                elif event.key == pygame.K_t:  # Press 't' to create a triangle
                    triangle = pygame.Rect(300, 300, 100, 100)
                    shapes.append(Shape("triangle", GREEN, triangle))

        for shape in shapes:
            shape.draw()

        pygame.display.flip()


if __name__ == "__main__":
    main()
