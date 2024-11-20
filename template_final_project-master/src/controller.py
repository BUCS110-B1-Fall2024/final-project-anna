import pygame
from frog import Frog
from obstacle import Obstacle
from points import Points
class Controller:
    def __init__(self):
        """
        Initializes the game controller to manage the Frog, Obstacle, and Points object.
        """
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Frog Jump Game")
        self.frog = Frog(x = -100, y = 0, width = 40, height = 40, img_file = "frog.png")
        self.obstacles = [Obstacle(x = 800, y = 0, width = 20, height = 40, img_file = "spikes.png")]
        self.points = [Points(x = 600, y =0, width = 20, height = 20, img_file = "lilypad.png")]
        self.running = True
    def handle_events(self):
        """
        If user needs to quit the game they could.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.frog.jump()
    def detect_collisions(self):
        """
        Checks for collisions.
        """
        for obstacle in self.obstacles:
            if obstacle.check_collision(self.frog.x, self.frog.y, self.frog.width, self.frog.height):
                print("Game Over.")
                self.running = False
        for points in self.points:
            if not points.collected and points.check_collision(self.frog.x, self.frog.y, self.frog.width, self.frog.height):
                points.collect()
                print("Point collected!")
    def update_models(self):
        """Updates game objects.
        """
        for obstacle in self.obstacles:
            obstacle.update_position()
        for point in self.points:
            point.x -= 5
        self.frog.update_position()
    def redraw(self):
        """Redraws objects pn the screen.
        """
        self.screen.fill((173, 216, 230))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.frog.x, self.frog.y, self.frog.width, self.frog.height))
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, (255, 0, 0), (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
        for points in self.points:
            pygame.draw.rect(self.screen, (0, 0, 255), (points.x, points.y, points.width, points.height))
    def mainloop(self):
        """Main game loop.
        """
        while self.running:
            self.handle_events()
            self.detect_collisions()
            self.update_models()
            self.redraw()
            pygame.display.flip()
            self.clock.tick(30)