import os
import random

import sqlite3

from Map import TXT_map, TXT_map_draw
from Counter_for_Animations import count, counter, num_count
from Locig_for_TXT import *
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class TXTGame(arcade.Window):
    def __init__(self):
        self.gladiator_list = arcade.SpriteList()
        num_count(self)
        self.miles = 0
        self.thirst = 0
        self.fatigue = 0
        self.pursuit = -20
        self.drink = 3

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
        TXT_map(self)

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
        if self.dialogue == False:
            count(self, x=5)
            arcade.start_render()
            TXT_map_draw(self)
            logic(self)
            arcade.draw_text('Troops of Sparta', 620, 776, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
            arcade.draw_text('[SPACE] - Пропустить/Окей', 1250, 38, arcade.csscolor.BLACK, font_size=15)
            if self.begin == True:
                begin(self)

            elif self.basic == True and self.begin == False:
                basic(self)

            elif self.drink_water == True and self.begin == False and self.basic == False:
                drink_water(self)

            elif self.slow_run == True and self.begin == False and self.basic == False:
                slow_run(self)
                dealer(self)

            elif self.fast_run == True and self.begin == False and self.basic == False:
                fast_run(self)
                dealer(self)

            elif self.sleep == True and self.begin == False and self.basic == False:
                sleep(self)

            elif self.status == True and self.begin == False and self.basic == False:
                status(self)



    def update(self, delta_time: float):
        if self.dialogue:
            self.dialoge.update()
        if self.dialogue == False:
            counter(self, x=5)
            try:
                self.gladiator_sprite = arcade.Sprite(f'Texture/Gladiator/r0.gif', scale=1)
            except:
                pass
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
        if self.dialogue == False:
            if self.Done == True:
                if key == arcade.key.ENTER:
                    arcade.close_window()
                    os.system('python main.py')
            elif self.Done == False:
                if key == arcade.key.R:
                    self.miles = 0
                    self.thirst = 0
                    self.fatigue = 0
                    self.pursuit = -15
                    self.drink = 3
            self.dear = random.randrange(20)
            if self.begin == True:
                if key == arcade.key.SPACE:
                    self.begin = False
            if self.begin == False:
                if key == arcade.key.KEY_1:
                    self.basic = False
                    self.drink_water = True
                    self.drink -= 1
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
                if self.basic == False:
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