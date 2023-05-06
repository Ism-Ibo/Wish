from main import *
from KNB import *
import arcade
main = True
KNB1 = False
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(1920, 1080, "My Game", fullscreen=True)
        self.main = True
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    if main == True:
        Main()
    elif KNB1 == True:
        KNB()
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.KEY_1:
            self.main = True
            self.KNB = False
        elif symbol == arcade.key.KEY_2:
            self.main = False
            self.KNB = True

window = MyGame()
arcade.run()
