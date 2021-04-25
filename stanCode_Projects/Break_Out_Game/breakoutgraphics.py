"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause


BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT, x=(window_width - PADDLE_WIDTH) / 2,
                            y=window_height - PADDLE_OFFSET)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2, x=(window_width - BALL_RADIUS)/2, y=(window_height - BALL_RADIUS)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.track)
        self.switch = 0

        # Draw bricks
        self.num_bricks = BRICK_ROWS*BRICK_COLS
        for i in range(BRICK_ROWS):
            for j in range(0, 2):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'tomato'
                self.brick.color = 'tomato'
                self.window.add(self.brick, (brick_spacing + brick_width)*i, (brick_spacing + brick_height)*j)
        for i in range(BRICK_ROWS):
            for j in range(2, 4):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'sandybrown'
                self.brick.color = 'sandybrown'
                self.window.add(self.brick, (brick_spacing + brick_width) * i, (brick_spacing + brick_height) * j)
        for i in range(BRICK_ROWS):
            for j in range(4, 6):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'gold'
                self.brick.color = 'gold'
                self.window.add(self.brick, (brick_spacing + brick_width) * i, (brick_spacing + brick_height) * j)
        for i in range(BRICK_ROWS):
            for j in range(6, 8):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'mediumseagreen'
                self.brick.color = 'mediumseagreen'
                self.window.add(self.brick, (brick_spacing + brick_width) * i, (brick_spacing + brick_height) * j)
        for i in range(BRICK_ROWS):
            for j in range(8, 10):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'blue'
                self.brick.color = 'blue'
                self.window.add(self.brick, (brick_spacing + brick_width) * i, (brick_spacing + brick_height) * j)

    def track(self, m):
        if m.x < PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif m.x > self.window.width-PADDLE_WIDTH/2:
            self.paddle.x = self.window.width-PADDLE_WIDTH
        else:
            self.paddle.x = m.x - PADDLE_WIDTH / 2

    def start(self, m):
        if self.switch == 0:
            self.switch += 1

    def ball_move(self):
        """
        Move ball by the change in x and y.
        """
        self.ball.move(self.__dx, self.__dy)

    def ball_reset(self):
        """
        Set ball position to the middle of window.
        """
        self.ball.x = (self.window.width - BALL_RADIUS)/2
        self.ball.y = (self.window.height - BALL_RADIUS)/2
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def hit_wall(self):
        """
        Update dx and dy while ball hits wall.
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def hit_object(self):
        """
        Update dx and dy while ball hits bricks or paddle.
        """
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS*2)
        obj3 = self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y)
        obj4 = self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y + BALL_RADIUS*2)
        if obj1 is not None and obj1.width == BRICK_WIDTH:
            self.window.remove(obj1)
            self.num_bricks -= 1
            self.__dy = -self.__dy
        elif obj2 is not None and obj2.width == BRICK_WIDTH:
            self.window.remove(obj2)
            self.num_bricks -= 1
            self.__dy = -self.__dy
        elif obj2 is not None and obj2.width == PADDLE_WIDTH:
            self.__dy = -self.__dy
        elif obj3 is not None and obj3.width == BRICK_WIDTH:
            self.window.remove(obj3)
            self.num_bricks -= 1
            self.__dy = -self.__dy
        elif obj4 is not None and obj4.width == BRICK_WIDTH:
            self.window.remove(obj4)
            self.num_bricks -= 1
            self.__dy = -self.__dy
        elif obj4 is not None and obj4.width == PADDLE_WIDTH:
            self.__dy = -self.__dy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
