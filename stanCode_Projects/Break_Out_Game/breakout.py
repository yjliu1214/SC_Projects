"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        if graphics.switch != 0:
            graphics.ball_move()
            graphics.hit_wall()
            graphics.hit_object()
            if graphics.ball.y >= graphics.window.height:
                graphics.switch -= 1
                lives -= 1
                graphics.ball_reset()
            if lives == 0 or graphics.num_bricks == 0:
                break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
