import arcade
SPRITE_SCALING = 1.5
MOVEMENT_SPEED = 1
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def texture_main_hero(self):
    self.player_sprite_list = arcade.SpriteList()
    self.player_sprite = arcade.AnimatedWalkingSprite()
    filename = "Texture/MainHero/WieldWeaponReaper-Sheet.png"
    image_location_list = [[48, 0, 48, 48],
                           [96, 0, 48, 48],
                           [144, 0, 48, 48],
                           [192, 0, 48, 48],
                           [240, 0, 48, 48],
                           [288, 0, 48, 48],
                           [336, 0, 48, 48],
                           [384, 0, 48, 48],
                           [432, 0, 48, 48],
                           ]
    self.player_sprite.stand_right_textures = \
        arcade.load_textures(filename, image_location_list, False)
    self.player_sprite.stand_left_textures = \
        arcade.load_textures(filename, image_location_list, True)
    self.player_sprite.texture_change_distance = 20
    self.player_sprite.center_x = SCREEN_WIDTH // 2
    self.player_sprite.center_y = SCREEN_HEIGHT // 2
    self.player_sprite_list.append(self.player_sprite)
    filename = "Texture/MainHero/HostileRunningReaper-Sheet.png"
    image_location_list = [[48, 0, 48, 48],
                           [96, 0, 48, 48],
                           [144, 0, 48, 48],
                           [192, 0, 48, 48],
                           [240, 0, 48, 48],
                           [288, 0, 48, 48],
                           [336, 0, 48, 48],
                           ]
    self.player_sprite.walk_right_textures = \
        arcade.load_textures(filename, image_location_list, False)
    self.player_sprite.walk_left_textures = \
        arcade.load_textures(filename, image_location_list, True)
    filename = 'Texture/MainHero/PassiveRunningReaper-Sheet.png'
    image_location_list = [[0, 0, 48, 48],
                           [48, 0, 48, 48],
                           [96, 0, 48, 48],
                           [144, 0, 48, 48],
                           [192, 0, 48, 48],
                           [240, 0, 48, 48],
                           [288, 0, 48, 48],
                           ]
    self.player_sprite.walk_up_textures = arcade.load_textures(filename, image_location_list, False)
    filename = 'Texture/MainHero/PassiveRunningReaper-Sheet1.png'
    image_location_list = [[0, 0, 48, 48],
                           [48, 0, 48, 48],
                           [96, 0, 48, 48],
                           [144, 0, 48, 48],
                           [192, 0, 48, 48],
                           [240, 0, 48, 48],
                           [288, 0, 48, 48],
                           ]
    self.player_sprite.walk_down_textures = arcade.load_textures(filename, image_location_list, False)


def player_draw(self):
    self.player_sprite_list.draw()


def player_update(self):
    self.player_sprite_list.update()
    self.player_sprite_list.update_animation()


def on_key_press_main_hero(self, key: int):
    if key == arcade.key.A:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    if key == arcade.key.D:
        self.player_sprite.change_x = MOVEMENT_SPEED
    if key == arcade.key.W:
        self.player_sprite.change_y = MOVEMENT_SPEED
    if key == arcade.key.S:
        self.player_sprite.change_y = -MOVEMENT_SPEED


def on_key_release_main_hero(self, key: int):
    if key == arcade.key.D or key == arcade.key.A:
        self.player_sprite.change_x = 0
    if key == arcade.key.W or key == arcade.key.S:
        self.player_sprite.change_y = 0
