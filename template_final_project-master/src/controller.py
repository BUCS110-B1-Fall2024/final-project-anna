import pygame
import random
from src.frog import Frog
from src.obstacle import Obstacle
from src.points import Points
class Controller:
    def __init__(self):
        """Initialize the game by setting up the screen, game objects, and game state.
        """
        pygame.init()
        self.setup_screen()
        self.setup_game_objects()
        self.setup_game_state()
    def setup_screen(self):
        """Set up the game screen, clock, and colors, for background and ground.
        """
        self.screen_width = 800
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Frog Run")
        self.clock = pygame.time.Clock()
        self.background_color = (173, 216, 230)
        self.ground_color = (0, 128, 0)
    def setup_game_objects(self):
        """Initialize the frog, obstacles, points, and other game-related objects.
        """
        self.frog = Frog(x=100, y=340, img_file="assets/frog.png", gravity=0.8, jump_strength=-15)
        self.obstacles = []
        self.points = []
        self.ground_level = 360
        self.ground_scroll = 0
        self.scroll_speed = 5
    def setup_game_state(self):
        """Initialize the game state variables, such as score and spawn timers.
        """
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.spawn_timer = 0
        self.state = "menu"
    def spawn_obstacle(self):
        """Spawn a new obstacle on the screen.
        """
        self.obstacles.append(
            Obstacle(
                x=self.screen_width,
                y=self.ground_level - 40,
                width=40,
                height=40,
                img_file="assets/spikes.png"
            )
        )
    def spawn_point(self):
        """Spawn a new lily pad point on the screen.
        """
        self.points.append(
            Points(
                x=self.screen_width + random.randint(200, 400),
                y=self.ground_level - 60,
                width=30,
                height=30,
                img_file="assets/lilypad.png"
            )
        )
    def handle_events(self):
        """Handle all user inputs and events such as quitting or jumping.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.frog.jump()
    def update_objects(self):
        """Update positions of all game objects (frog, obstacles, points).
        """
        self.frog.update_position()
        self.update_obstacles()
        self.update_points()
    def update_obstacles(self):
        """Update the positions of all obstacles.
        """
        for obstacle in self.obstacles:
            obstacle.update_position()
        self.obstacles = [o for o in self.obstacles if not o.is_off_screen()]
    def update_points(self):
        """Update the positions of all lily pads.
        """
        for point in self.points:
            point.x -= self.scroll_speed
        self.points = [p for p in self.points if p.x + p.width > 0]
    def check_collisions(self):
        """Check if the frog has collided with any obstacles or collected points.
        """
        for obstacle in self.obstacles:
            if obstacle.collision(self.frog.x, self.frog.y, self.frog.width, self.frog.height):
                print("Game Over!")
                self.running = False
        self.collect_points()
    def collect_points(self):
        """Check if the frog has collected any lily pad points.
        """
        for point in self.points:
            if not point.collected and point.check_collision(self.frog.x, self.frog.y, self.frog.width, self.frog.height):
                point.collect()
                self.score += 1
    def manage_spawns(self):
        """Manage the spawning of obstacles and points at regular intervals.
        """
        self.spawn_timer += 1
        if self.spawn_timer % 120 == 0:
            self.spawn_obstacle()
        if self.spawn_timer % 180 == 0:
            self.spawn_point()
    def draw_background(self):
        """Draw the game background and the scrolling ground.
        """
        self.screen.fill(self.background_color)
        self.ground_scroll = (self.ground_scroll - self.scroll_speed) % self.screen_width
        pygame.draw.rect(self.screen, self.ground_color, (0, self.ground_level, self.screen_width, 40))
    def draw_objects(self):
        """Draw the frog, obstacles, points, and the score on the screen.
        """
        self.draw_frog()
        self.draw_obstacles()
        self.draw_points()
        self.draw_score()
    def draw_frog(self):
        """Draw the frog's image on the screen.
        """
        frog_img = pygame.image.load(self.frog.img_file).convert_alpha()
        frog_img = pygame.transform.scale(frog_img, (self.frog.width, self.frog.height))
        self.screen.blit(frog_img, (self.frog.x, self.frog.y))
    def draw_obstacles(self):
        """Draw each obstacle's image on the screen.
        """
        for obstacle in self.obstacles:
            obstacle_img = pygame.image.load(obstacle.img_file).convert_alpha()
            obstacle_img = pygame.transform.scale(obstacle_img, (obstacle.width, obstacle.height))
            self.screen.blit(obstacle_img, (obstacle.x, obstacle.y))
    def draw_points(self):
        """Draw each lily pad point's image on the screen.
        """
        for point in self.points:
            if not point.collected:
                point_img = pygame.image.load(point.img_file).convert_alpha()
                point_img = pygame.transform.scale(point_img, (point.width, point.height))
                self.screen.blit(point_img, (point.x, point.y))
    def draw_score(self):
        """Draw the current score on the screen.
        """
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
    def mainloop(self):
        """Main game loop that handles game states and updates the screen.
        """
        while self.running:
            if self.state == "menu":
                self.show_menu()
            elif self.state == "playing":
                self.handle_events()
                self.update_objects()
                self.check_collisions()
                self.manage_spawns()
                self.draw_background()
                self.draw_objects()
                if self.score >= 10:
                    self.state = "game_over"
            elif self.state == "game_over":
                self.show_game_over()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
    def show_menu(self):
        """Display the menu screen with instructions to start the game.
        """
        self.screen.fill(self.background_color)
        title_text = self.font.render("Frog Run Game", True, (0, 0, 0))
        play_text = self.font.render("Press SPACE to Start", True, (0, 0, 0))
        self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 150))
        self.screen.blit(play_text, (self.screen_width // 2 - play_text.get_width() // 2, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "playing"
    def show_game_over(self):
        """Display the game over screen with the final score and option to restart.
        """
        self.screen.fill(self.background_color)
        game_over_text = self.font.render("Game Over!", True, (255, 0, 0))
        score_text = self.font.render(f"Final Score: {self.score}", True, (0, 0, 0))
        restart_text = self.font.render("Press R to Restart", True, (0, 0, 0))
        self.screen.blit(game_over_text, (self.screen_width // 2 - game_over_text.get_width() // 2, 150))
        self.screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, 200))
        self.screen.blit(restart_text, (self.screen_width // 2 - restart_text.get_width() // 2, 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset_game()
    def reset_game(self):
        """Reset the game state and objects to restart the game.
        """
        self.setup_game_objects()
        self.setup_game_state()
        self.state = "menu"
