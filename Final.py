import arcade
import sqlite3

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class Final(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Final", fullscreen=True)
        self.image = None
        self.texture = None
        self.dialoge = None
        self.dialoge_num = None
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def setup(self):
        with sqlite3.connect('baza.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                sparta INTEGER,
                space INTEGER,
                knb INTEGER
                )""")
            cur.execute(
                f"""UPDATE users SET knb = 0, space = 0, sparta = 0""")
            cur.execute("""SELECT * FROM users""")
            con.commit()
        self.dialoge_num = 0
        self.dialoge = arcade.Sprite()

    def on_draw(self):
        arcade.start_render()
        self.dialoge.draw()
        arcade.draw_text('[ESC] - exit', 30, 30, arcade.csscolor.BLACK, font_size=15,
                         font_name='Showcard Gothic')
        self.image = f'Texture/Final/final{self.dialoge_num}.png'
        self.texture = arcade.load_texture(self.image)
        self.dialoge = arcade.Sprite()
        self.dialoge.center_x = 850
        self.dialoge.center_y = 450
        self.dialoge.texture = self.texture

    def on_update(self, delta_time: float):
        self.dialoge.update()

    def on_key_press(self, key: int, modifiers: int):
        if self.dialoge_num > 0:
            if key == arcade.key.LEFT:
                self.dialoge_num -= 1

        if self.dialoge_num < 5:
            if key == arcade.key.RIGHT:
                self.dialoge_num += 1
        if key == arcade.key.ESCAPE:
            arcade.exit()


def main():
    window = Final()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
