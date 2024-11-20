class Frog:
    def __init__(self, x = 0, y = 0, img_file = "frog.png", gravity = -9.8, jump_strength = 15):
        """Initialize the player object which is a frog and jump.

        args:
            x (int): the x position of where the frog position is
            y (int): the y position of where the frog position is
            img_file (str): The file for the frog's image
        """
        self.x = x
        self.y = y
        self.ground_level = y
        self.img_file = img_file
        self.gravity = gravity
        self.jump_strength = jump_strength
        self.on_ground = True
        self.velocity_y = 0
    def jump(self):
        """Makes the frog jump
        args: None
        return: None
        """
        if self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False
    def update_position(self):
        """Updates the position of the Frog when jumping
        args: None
        return: None
        """
        if not self.on_ground:
            self.velocity_y += self.gravity
            self.y += self.velocity_y
            if self.y <= self.ground_level:
                self.y = self.ground_level
                self.velocity_y = 0
                self.on_ground = True