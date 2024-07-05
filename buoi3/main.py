import pygame
from classes.ball import Ball
from classes.paddle import Paddle
from classes.player import Player


class Main:
    def __init__(
        self,
        title,
        size,
        bg,
        ball_img_link,
        paddle_img_link,
        ball_speed,
        ball_location,
        paddle_1_location,
        paddle_2_location,
    ) -> None:
        # setup canvas
        pygame.init()
        pygame.display.set_caption(title)
        self.canvas = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.bg = bg
        self.ball_img_link = ball_img_link
        self.paddle_img_link = paddle_img_link
        # create objects (player, ball, paddles)
        self.ball = Ball(
            img_url=ball_img_link, speed_x=ball_speed[0], speed_y=ball_speed[1]
        )
        self.paddle_1 = Paddle(img_url=paddle_img_link)
        self.paddle_2 = Paddle(img_url=paddle_img_link)
        self.player = Player()
        # setup location for objects
        self.ball.setX(x=ball_location[0])
        self.ball.setY(y=ball_location[1])
        self.paddle_1.setX(x=paddle_1_location[0])
        self.paddle_1.setY(y=paddle_1_location[1])
        self.paddle_2.setX(x=paddle_2_location[0])
        self.paddle_2.setY(y=paddle_2_location[1])

    def run(self):
        while True:  # play game
            events = pygame.event.get()  # bat su kien
            for e in events:
                # quit
                if e.type == pygame.QUIT:
                    return
                # keyboard check
                elif e.type == pygame.KEYDOWN:  # nhan phim
                    if e.key == pygame.K_w:
                        self.player.setKeyUp1(True)
                    elif e.key == pygame.K_s:
                        self.player.setKeyDown1(True)
                    elif e.key == pygame.K_UP:
                        self.player.setKeyUp2(True)
                    elif e.key == pygame.K_DOWN:
                        self.player.setKeyDown2(True)

                elif e.type == pygame.KEYUP:  # khong nhan phim
                    if e.key == pygame.K_w:
                        self.player.setKeyUp1(False)
                    elif e.key == pygame.K_s:
                        self.player.setKeyDown1(False)
                    elif e.key == pygame.K_UP:
                        self.player.setKeyUp2(False)
                    elif e.key == pygame.K_DOWN:
                        self.player.setKeyDown2(False)

            self.ball.move(
                paddle_1_x=self.paddle_1.getX(),
                paddle_1_y=self.paddle_1.getY(),
                paddle_1_distance=30,
                paddle_2_x=self.paddle_2.getX(),
                paddle_2_y=self.paddle_2.getY(),
                paddle_2_distance=-30,
            )

            # kiem tra nut bam de di chuyen paddles
            if self.player.getKeyUp1():
                self.paddle_1.move(direction=-1, bound_top=0, bound_down=480)
            if self.player.getKeyDown1():
                self.paddle_1.move(1, 0, 480)
            if self.player.getKeyUp2():
                self.paddle_2.move(-1, 0, 480)
            if self.player.getKeyDown2():
                self.paddle_2.move(1, 0, 480)

            # show canvas
            self.canvas.fill(self.bg)
            self.canvas.blit(self.ball.img_url, (self.ball.getX(), self.ball.getY()))
            self.canvas.blit(
                self.paddle_1.img, (self.paddle_1.getX(), self.paddle_1.getY())
            )
            self.canvas.blit(
                self.paddle_2.img, (self.paddle_2.getX(), self.paddle_2.getY())
            )
            self.clock.tick(60)
            pygame.display.flip()
# time and end
# game_time = 30
# white = (225, 225, 225)
# black = (0, 0, 0)
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 36)

# def draw_text(text, font, color, surface, x ,y):
#     textobj = font.render(text, True, color)
#     textrect = textobj.get_rect()
#     textrect.topleft = (x,y)
#     surface.blit(textobj, textrect)

# def game_over_screen():
#     set.fill(black)
#     draw_text("Game Over", font, while, screen, 250, 200)
#     draw_text("press any key to restart", small_font, white, canvas, 220, 300)
#     pygame.display.flip()
#     waiting_for_restart = True
#     while waiting_for_restart:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 waiting_for_restart = False
#                 main()

def time_couter(self):
    self.time -= 1/60
    if self.time < 25:
        self.end()

def show_time(self):
    if self.time > 25:
        if pygame.font:
            font = pygame.font.Font(None, 36)
            time = font.render(f"time left:{self.time:.0f}", 1, (225, 225, 225))
            self.canvas.blit(time, (0, 0))

def end(self):
    self.canvas.fill(self.end_bg)
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("END", 1, (225, 225, 225))
        self.canvas.blit(text, (275, 280))
# Driver code
main = Main(
    title="Ping Pong",
    size=(600, 600),
    bg=(252, 16, 140),
    ball_img_link="D:\\Python2\\buoi3\\acset\\ball.png",
    paddle_img_link="D:\\Python2\\buoi3\\acset\\paddle.png",
    ball_location=(285, 300),
    ball_speed=(1.5, 3.5),
    paddle_1_location=(0, 250),
    paddle_2_location=(570, 250),
)
main.run()