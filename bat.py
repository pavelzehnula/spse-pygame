from pgzero.actor import Actor

from conf import SCREEN_HEIGHT, SCREEN_WIDTH


class Bat(Actor):
    INIT_POSITION = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
    __speed = 5
    __img_name = "paddle_blu"

    def __init__(self):
        super().__init__(self.__img_name, self.INIT_POSITION)

    def update(self):
        pass

    def move_right(self):
        """
        Pohyb doprava. Posuneme bod left o hodnotu speed
        :return:
        """
        self.left += self.__speed

    def move_left(self):
        """
        Pohyb doleva. Snížíme bod left o hodnotu speed
        :return:
        """
        self.left -= self.__speed
