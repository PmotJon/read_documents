import pygame
import random


class snake_game:
    # Constructor oop
    def __init__(self):
        pygame.init()

        # colors
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)

        # ukuran
        self.dis_width = 600
        self.dis_height = 400

        # layar
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))

        # Beri judul pada layar
        pygame.display.set_caption("snake game")

        # clock
        self.clock = pygame.time.Clock()
        # Ukuran blok snake kecepatan
        self.snake_block = 10
        self.snake_speed = 5
        # tentukan font style
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 25)

        self.game_over = False
        self.game_close = False
        # koordinat kepala
        self.x1 = self.dis_width / 2
        self.y1 = self.dis_height / 2
        # variabel
        self.x1_change = 0
        self.y1_change = 0

        self.snake_List = []

        self.Length_of_snake = 1

        self.foodx = (
            round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        )
        self.foody = (
            round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
        )

    # Def fungsi
    def Your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.yellow)
        self.dis.blit(value, [0, 0])

    # Def fungsi untuk menggambar snake
    def our_snake(self, snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(
                self.dis, self.black, [x[0], x[1], snake_block, snake_block]
            )

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def gameLoop(self):
        # Loop
        while not self.game_over:
            while self.game_close:
                self.dis.fill(self.blue)
                self.message("You lost, press c to play again or Q to quit", self.red)
                self.Your_score(self.Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                            if event.key == pygame.K_c:
                                self.__init__()
                                self.gameLoop()
            # checking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.y1_change = -self.snake_block
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y1_change = self.snake_block
                        self.x1_change = 0
            if (
                self.x1 >= self.dis_width
                or self.x1 < 0
                or self.y1 >= self.dis_height
                or self.y1 < 0
            ):
                self.game_close = True
            # gerakan
            self.x1 += self.x1_change
            self.x1 += self.y1_change
            self.dis.fill(self.blue)
            pygame.draw.rect(
                self.dis,
                self.green,
                [self.foodx, self.foody, self.snake_block, self.snake_block],
            )
            snake_head = [self.x1, self.y1]
            self.snake_List.append(snake_head)
            if len(self.snake_List) > self.Length_of_snake:
                del self.snake_List[0]

            for x in self.snake_List[:-1]:
                if x == snake_head:
                    self.game_close = True
            self.our_snake(self.snake_block, self.snake_List)
            self.Your_score(self.Length_of_snake - 1)
            # Update
            pygame.display.update()

            if self.x1 == self.foodx and self.y1 == self.foody:
                self.foodx = (
                    round(random.randrange(0, self.dis_width - self.snake_block) / 10.0)
                    * 10.0
                )
                self.foody = (
                    round(
                        random.randrange(0, self.dis_height - self.snake_block) / 10.0
                    )
                    * 10.0
                )
                self.Length_of_snake += 1
            self.clock.tick(self.snake_speed)
        pygame.quit()
        quit()


if __name__ == "__main__":
    game = snake_game()
    game.gameLoop()
