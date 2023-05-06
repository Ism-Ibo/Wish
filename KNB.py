import os
import arcade.key
import sqlite3
from Map import KNB_map, KNB_map_draw
from Logic_for_KNB import *
from Counter_for_Animations import num_count, count, counter
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class MyKNB(arcade.Window):


    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game", fullscreen=True)
        num_count(self)
        self.start = True
        self.Done = False
        self.npc_sprite = None
        self.npc_list = None
        self.player_sprite = None
        self.player_list = None
        self.random_npc = 0
        self.player_number = 0
        self.player_score = 0
        self.npc_score = 0
        # NPC UPDATE
        self.npc_sprite = arcade.Sprite(f'Texture/KNB/k0.gif', scale=1)
        self.npc_sprite.center_x = 1275
        self.npc_sprite.center_y = 674
        self.npc_sprite_list = arcade.SpriteList()
        self.npc_sprite_list.append(self.npc_sprite)
        self.death_sprite = arcade.Sprite(f'Texture/KNB/h0.gif', scale=1)
        self.death_sprite.center_x = 227
        self.death_sprite.center_y = 194
        self.death_list = arcade.SpriteList()
        self.death_list.append(self.death_sprite)
        self.dialoge_num = 0
        self.dialoge = arcade.Sprite()
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)



    def setup(self):

        KNB_map(self)

    def on_key_press(self, key: int, modifiers: int):
        if self.start == False:
            if key == arcade.key.Q:
                Q(self)
            elif key == arcade.key.W:
                W(self)
            elif key == arcade.key.E:
                E(self)

            if key == arcade.key.R:
                self.player_score = 0
                self.npc_score = 0
            if self.Done == True:
                if key == arcade.key.ENTER:
                    self.player_score = 0
                    self.npc_score = 0
                    arcade.close_window()
                    os.system("python main.py")
        if key == arcade.key.SPACE:
            self.start = False
        if self.start:
            if self.dialoge_num > 0:
                if key == arcade.key.LEFT:
                    self.dialoge_num -= 1
                    print('h')
            if self.dialoge_num < 9:
                if key == arcade.key.RIGHT:
                    self.dialoge_num += 1
        if key == arcade.key.ESCAPE:
            arcade.exit()




    def on_draw(self):
        if self.start:
            arcade.start_render()
            self.dialoge.draw()
            arcade.draw_text('[SPACE] - start', 1360, 30, arcade.csscolor.BLACK, font_size=15,
                             font_name='Showcard Gothic')
            arcade.draw_text('[<]/[>] - dialogue', 30, 30, arcade.csscolor.BLACK, font_size=15,
                             font_name='Showcard Gothic')
            self.image = f'Texture/KNB/Kov/kov{self.dialoge_num}.png'
            self.texture = arcade.load_texture(self.image)
            self.dialoge = arcade.Sprite()
            self.dialoge.center_x = 850
            self.dialoge.center_y = 450
            self.dialoge.texture = self.texture



        if self.start == False:
            count(self)
            arcade.start_render()
            KNB_map_draw(self)
            self.death_list.draw()
            self.npc_sprite_list.draw()
            arcade.draw_circle_outline(461, 71, 11, arcade.csscolor.BLACK)
            arcade.draw_circle_outline(461, 111, 11, arcade.csscolor.BLACK)
            arcade.draw_circle_outline(461, 151, 11, arcade.csscolor.BLACK)
            if self.player_score == 1:
                arcade.draw_circle_filled(461, 71, 10, arcade.csscolor.DARK_RED)
            elif self.player_score == 2:
                arcade.draw_circle_filled(461, 71, 10, arcade.csscolor.DARK_RED)
                arcade.draw_circle_filled(461, 111, 10, arcade.csscolor.DARK_RED)
            elif self.player_score == 3:
                arcade.draw_circle_filled(461, 71, 10, arcade.csscolor.DARK_RED)
                arcade.draw_circle_filled(461, 111, 10, arcade.csscolor.DARK_RED)
                arcade.draw_circle_filled(461, 151, 10, arcade.csscolor.DARK_RED)
            arcade.draw_circle_outline(1069, 710, 11, arcade.csscolor.BLACK)
            arcade.draw_circle_outline(1069, 750, 11, arcade.csscolor.BLACK)
            arcade.draw_circle_outline(1069, 790, 11, arcade.csscolor.BLACK)
            if self.npc_score == 1:
                arcade.draw_circle_filled(1069, 710, 10, arcade.csscolor.DARK_BLUE)
            elif self.npc_score == 2:
                arcade.draw_circle_filled(1069, 710, 10, arcade.csscolor.DARK_BLUE)
                arcade.draw_circle_filled(1069, 750, 10, arcade.csscolor.DARK_BLUE)
            elif self.npc_score == 3:
                arcade.draw_circle_filled(1069, 710, 10, arcade.csscolor.DARK_BLUE)
                arcade.draw_circle_filled(1069, 750, 10, arcade.csscolor.DARK_BLUE)
                arcade.draw_circle_filled(1069, 790, 10, arcade.csscolor.DARK_BLUE)
            arcade.draw_text('Q - Paper', 20, 810, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
            arcade.draw_text('W - Rock', 20, 750, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
            arcade.draw_text('E - Scissors', 20, 690, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
            if self.player_score >= 3:
                with sqlite3.connect('baza.db') as con:
                    cur = con.cursor()
                    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                        sparta INTEGER,
                        space INTEGER,
                        knb INTEGER
                        )""")
                    cur.execute(
                        f"""UPDATE users SET knb = 1""")
                    cur.execute("""SELECT * FROM users""")

                    con.commit()
                arcade.draw_text('You Win', 695, 427, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
                self.Done = True
                arcade.draw_text('[ENTER] - back', 680, 400, arcade.csscolor.BLACK, font_size=15, font_name='Showcard Gothic')

            elif self.npc_score >= 3:
                arcade.draw_text('Game Over', 680, 427, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
                arcade.draw_text('R - replay', 680, 400, arcade.csscolor.BLACK, font_size=15, font_name='Showcard Gothic')
            elif self.random_npc == 1 and self.player_number == 1 or self.random_npc == 2 and self.player_number == 2 or self.random_npc == 3 and self.player_number == 3:
                arcade.draw_text('Draw', 710, 427, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
            try:

                self.player_list.draw()
                self.npc_list.draw()
                self.game_over.draw()
            except:
                pass


    def update(self, delta_time):
        counter(self)
        try:
            self.player_list.update()
            self.npc_list.update()
        except:
            pass

        self.npc_sprite_list.update()
        #PLAYER UPDATE

        self.dialoge.update()
        self.death_list.update()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)


def main():
    window = MyKNB()
    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()