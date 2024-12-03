class Points:
    def __init__(self, x, y, width, height, img_file):
        """Initializes the Lily pads which are the point objects.

        args:
            x (int): The x coordinate of the lily pads.
            y (int): The y coordinate of the lily pads.
            width (int): The width of the lily pads.
            height (int): The height of the lily pads.
            img_file (str): The file for the Lily pads.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img_file = img_file
        self.collected = False
    def check_collision(self, frog_x, frog_y, frog_width, frog_height):
        """Checks if the frog collided with the lily pads.
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
    def collect(self):
        """Marks the lily pad as collected object.
        args: None
        return: None
        """
        self.collected = True