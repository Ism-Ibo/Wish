import arcade

from NPC import *
from Hero import player_draw, player_update, on_key_press_main_hero, on_key_release_main_hero, texture_main_hero
import os
import sqlite3
from Counter_for_DEATH import num_countd, countd, counterd
from Counter_for_Animations import num_count, count, counter
from Map import map, map_draw, map_update

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
CAMERA_SPEED = 0.5

class MyGame(arcade.Window):


    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game", fullscreen=True)
        texture_main_hero(self)
        num_count(self)
        num_countd(self)
        self.kovboy = False
        self.sparta = False
        self.space = False
        self.death = True
        self.start = True
        self.santa_list = arcade.SpriteList()
        self.gladiator_list = arcade.SpriteList()
        self.goblin_list = arcade.SpriteList()
        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE )


    def setup(self):
        map(self)
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.wish_sprite = arcade.Sprite(f'Texture/KNB/h0.gif', scale=1)
        self.wish_sprite.center_x = 240
        self.wish_sprite.center_y = 533
        self.wish_list = arcade.SpriteList()
        self.wish_list.append(self.wish_sprite)
        with sqlite3.connect('baza.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                sparta INTEGER,
                space INTEGER,
                knb INTEGER
                )""")
            cur.execute("""SELECT * FROM users""")
            result = cur.fetchall()


            con.commit()
        self.Final = False
        self.done_TXT = result[-1][0]
        self.done_Space = result[-1][1]
        self.done_KNB = result[-1][2]
        if self.done_KNB == 1 and self.done_Space == 1 and self.done_TXT:
            self.Final = True



    def on_draw(self):
        if self.start:
            arcade.start_render()
            self.wish_list.draw()
            arcade.draw_text('Wish Ibo', 800, 781, arcade.csscolor.BLACK, font_size=40, font_name='Showcard Gothic')
            arcade.draw_text('Привет, меня зовут Ибо. Я виш, слуга смерти!', 469, 645, arcade.csscolor.BLACK, font_size=24)
            arcade.draw_text('Вряд ли вы слышали про таких существ, как я, ведь мы есть', 469, 600, arcade.csscolor.BLACK,
                             font_size=24)
            arcade.draw_text('не в кажддой вселенной. Но в моей вселенной я один из первых', 469,
                             555, arcade.csscolor.BLACK,
                             font_size=24)
            arcade.draw_text(
                'представителей своегшо рода.', 469,
                515, arcade.csscolor.BLACK,
                font_size=24)
            arcade.draw_text(
                'Вы спросите почему мы тут собрались, а я отвечу:', 469,
                470, arcade.csscolor.BLACK,
                font_size=24)
            arcade.draw_text(
                '"Что бы я вам рассказал историю как я спас свою Вселенную ', 469,
                425, arcade.csscolor.BLACK,
                font_size=24)
            arcade.draw_text(
                'от вредителей используя дар Смерти за миллиардное исполненное желания"', 469,
                380, arcade.csscolor.BLACK,
                font_size=24)
            arcade.draw_text(
                'исполненное желания."', 469,
                335, arcade.csscolor.BLACK,
                font_size=24)
            arcade.draw_text(
                'Всё началось в день когда мне осталось 3 желания что бы мой счёт дошёл до миллиарда...', 70,
                140, arcade.csscolor.BLACK,
                font_size=24)
            arcade.draw_text('[SPACE] - start', 1360, 30, arcade.csscolor.BLACK, font_size=15, font_name='Showcard Gothic')
        if self.start == False:
            self.camera_sprites.use()
            count(self)
            countd(self)
            arcade.start_render()


            map_draw(self)
            player_draw(self)
            #snake_draw(self)



            if self.done_KNB != 1:
                if arcade.check_for_collision_with_list(self.player_sprite, self.map_list_Di):
                    self.kovboy = True
                santa_draw(self)
            if self.done_TXT != 1:
                if arcade.check_for_collision_with_list(self.player_sprite, self.map_list_Sparta):
                    self.sparta = True
                Gladiator_draw(self)

            if self.done_Space != 1:
                if arcade.check_for_collision_with_list(self.player_sprite, self.map_list_Space1):
                    self.space = True
                goblin_draw(self)

            if self.Final:

                death_draw(self)



            if arcade.check_for_collision_with_list(self.player_sprite, self.map_list_Death):
                self.death = True



    def update(self, delta_time):
        counter(self)
        counterd(self)
        #snake_update(self)
        map_update(self)
        player_update(self, delta_time)
        Gladiator_update(self)
        if self.done_KNB != 0:
            santa_update(self)
        goblin_update(self)
        death_update(self)
        self.scroll_to_player()
        self.wish_list.update()


    def on_key_press(self, key: int, modifiers: int):
        on_key_press_main_hero(self, key, modifiers)

        if key == arcade.key.ENTER:
            if self.done_KNB != 1:
                if self.kovboy == True:
                    arcade.close_window()
                    os.system('python KNB.py')
            if self.done_TXT != 1:
                if self.sparta == True:
                    arcade.close_window()
                    os.system('python TXT.py')
            if self.done_Space != 1:
                if self.space == True:
                    arcade.close_window()
                    os.system('python Space.py')
            if self.Final:
                if self.death == True:
                    arcade.close_window()
                    os.system('python Final.py')
        if key == arcade.key.ESCAPE:
            arcade.exit()

        if self.start:
            if key == arcade.key.SPACE:
                self.start = False










    def on_key_release(self, key: int, modifiers: int):
        on_key_release_main_hero(self, key, modifiers)


    def scroll_to_player(self):
        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)


    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)







def main():

    window = MyGame()
    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()



