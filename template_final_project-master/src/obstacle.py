class Obstacle:
    def __init__(self, x = 10, y = 0, width = 2, height = 2 , img_file = "spikes.png"):
        """Initialize the Obstacle object.

        args:
            x (int): The x coordinate of the obstacle.
            y (int): The y coordinate of the obstacle.
            width (int): The width of the obstacle.
            height (int): The height of the obstacle.
            img_file (str): The file for the obstacle's image.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img_file = img_file
        self.speed = 5
    def update_position(self):
        """Updates the obstacle's position and it moves the obstacle to the left of the screen.
        args: None
        return: None
        """
        self.x -= self.speed
    def is_off_screen(self):
        """Checks if the obstacle is off screen.
        args: None
        return:
            bool: True if the obstacle is off the screen, False if it is not off the screen.
        """
        return self.x + self.width < 0
    def get_position(self):
        """Gets the positioin of the obstacle.
        args: None
        return:
            turple: (x, y) position of the obstacle.
        """
        return self.x, self.y
    def collision(self, frog_x, frog_y, frog_width, frog_height):
        """Checks if the frog collided with the obstacle.
        args:
            frog_x (int): The x coordinate of the frog.
            frog_y (int): The y coordinate of the frog.
            frog_width (int): The width of the frog.
            frog_height (int): The height of the frog.
        return:
            bool: True if the frog collided with the obstacle, Flase if it didn't.
        """
        right_side = self.x + self.width > frog_x
        left_side = self.x < frog_x + frog_width
        bottom = self.y +self.height > frog_y
        top = self.y < frog_y + frog_height
        return right_side and left_side and bottom and top