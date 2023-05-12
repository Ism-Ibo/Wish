import os
import random


from Map import txt_map, txt_map_draw
from Locig_for_TXT import *
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864


class TXTGame(arcade.Window):
    def __init__(self):
        self.gladiator_list = arcade.SpriteList()
        self.miles = 0
        self.thirst = 0
        self.fatigue = 0
        self.pursuit = -20
        self.drink = 4

        self.gladiator_sprite = None
        self.dear = None
        self.random_slow_miles = None
        self.random_miles = None
        self.image = None
        self.texture = None

        self.begin = False
        self.basic = False
        self.drink_water = False
        self.slow_run = False
        self.fast_run = False
        self.sleep = False
        self.status = False

        self.Done = False

        self.dialogue = True
        self.dialoge = arcade.Sprite()
        self.dialoge_num = 0
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'TXT', fullscreen=True)
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def setup(self):
        txt_map(self)

    def on_draw(self):
        if self.dialogue:
            arcade.start_render()
            arcade.draw_text('[ENTER] - start', 1360, 30, arcade.csscolor.BLACK, font_size=15,
                             font_name='Showcard Gothic')
            arcade.draw_text('[<]/[>] - dialogue', 30, 30, arcade.csscolor.BLACK, font_size=15,
                             font_name='Showcard Gothic')
            self.image = f'Texture/TXT/Voin/voin{self.dialoge_num}.png'
            self.texture = arcade.load_texture(self.image)
            self.dialoge = arcade.Sprite()
            self.dialoge.center_x = 850
            self.dialoge.center_y = 450
            self.dialoge.texture = self.texture
            self.dialoge.draw()
        if self.dialogue == 0:

            arcade.start_render()
            txt_map_draw(self)
            logic(self)
            arcade.draw_text('Troops of Sparta', 620, 776, arcade.csscolor.BLACK,
                             font_size=24, font_name='Showcard Gothic')
            arcade.draw_text('[SPACE] - Skip/Continue', 1250, 38, arcade.csscolor.BLACK,
                             font_size=15, font_name='Showcard Gothic')
            if self.begin:
                begin(self)

            elif self.basic and self.begin == 0:
                basic()

            elif self.drink_water and self.begin == 0 and self.basic == 0:
                drink_water(self)

            elif self.slow_run and self.begin == 0 and self.basic == 0:
                slow_run(self)
                dealer(self)

            elif self.fast_run and self.begin == 0 and self.basic == 0:
                fast_run(self)
                dealer(self)

            elif self.sleep and self.begin == 0 and self.basic == 0:
                sleep(self)

            elif self.status and self.begin == 0 and self.basic == 0:
                status(self)

    def update(self, delta_time: float):
        if self.dialogue:
            self.dialoge.update()
        if self.dialogue == 0:
            self.gladiator_sprite = arcade.Sprite(f'Texture/Gladiator/r0.gif', scale=1)
            self.gladiator_sprite.center_x = 820
            self.gladiator_sprite.center_y = 262
            self.gladiator_list = arcade.SpriteList()
            self.gladiator_list.append(self.gladiator_sprite)
            self.gladiator_list.update()

    def on_key_press(self, key: int, modifiers: int):
        if self.dialogue:
            if key == arcade.key.ENTER:
                self.begin = True
                self.dialogue = False
            if self.dialoge_num > 0:
                if key == arcade.key.LEFT:
                    self.dialoge_num -= 1

            if self.dialoge_num < 16:
                if key == arcade.key.RIGHT:
                    self.dialoge_num += 1
        if self.dialogue == 0:
            if self.Done:
                if key == arcade.key.ENTER:
                    arcade.close_window()
                    os.system('python main.py')
            elif self.Done == 0:
                if key == arcade.key.R:
                    self.miles = 0
                    self.thirst = 0
                    self.fatigue = 0
                    self.pursuit = -15
                    self.drink = 3
                    self.basic = True
            self.dear = random.randrange(20)
            if self.begin:
                if key == arcade.key.SPACE:
                    self.begin = False
            if self.begin == 0:
                if key == arcade.key.KEY_1:
                    self.basic = False
                    self.drink_water = True
                    if self.drink > 0:
                        self.drink -= 1
                    if self.drink > 0:
                        self.thirst = 0
                elif key == arcade.key.KEY_2:
                    self.basic = False
                    self.slow_run = True
                    self.random_slow_miles = random.randint(5, 13)
                    random_pursuit = random.randint(7, 14)
                    self.fatigue += 1
                    self.miles += self.random_slow_miles
                    self.pursuit += random_pursuit
                    self.thirst += 1
                elif key == arcade.key.KEY_3:
                    self.basic = False
                    self.fast_run = True
                    random_fatigue = random.randint(1, 3)
                    self.random_miles = random.randint(10, 17)
                    random_pursuit = random.randint(7, 14)
                    self.fatigue += random_fatigue
                    self.miles += self.random_miles
                    self.pursuit += random_pursuit
                    self.thirst += 1
                elif key == arcade.key.KEY_4:
                    self.basic = False
                    self.sleep = True
                    random_pursuit = random.randint(7, 14)
                    self.pursuit += random_pursuit
                    self.fatigue = 0
                elif key == arcade.key.KEY_5:
                    self.basic = False
                    self.status = True
                if self.basic == 0:
                    if key == arcade.key.SPACE:
                        self.drink_water = False
                        self.slow_run = False
                        self.fast_run = False
                        self.sleep = False
                        self.status = False
                        self.basic = True
        if key == arcade.key.ESCAPE:
            arcade.exit()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(x, y)


def main():
    window = TXTGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
