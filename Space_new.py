import random
import os
import sqlite3

import pygame
import arcade
from Map import space_map, space_map_draw, space_map_update
from logic_for_Space import main_hero, main_hero_draw, main_hero_update, main_hero_controller, fire_speed,\
    engine_counter, weapon_counter, fire_speed_update, fire_speed_draw, planet_counter, space_count

pygame.init()
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864
SPEED = 2
BULLET_COOLDOWN = 0.2
BULLET_SPEED = 10


class Space(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'GalaxyWar', fullscreen=True)
        self.explosions_list = None
        self.explosions_boss_list = None
        self.explosions_asteroid_list = None
        self.dialoge = None
        self.ship_weapon_list = None
        self.npc_list = None
        self.npc_bullet_list = None
        self.speed_npc_weapons = None
        self.npc1 = None
        self.npc2 = None
        self.npc3 = None
        self.npc4 = None
        self.npc5 = None
        self.npc6 = None
        self.npc7 = None
        self.npc8 = None
        self.npc9 = None
        self.asteroid_list = None
        self.asteroid = None
        self.last_asteroid = None
        self.boss_num = None
        self.boss_count = None
        self.boss_height = None
        self.boss_y = None
        self.boss_asteroid = None
        self.boss_list = None
        self.boss1 = None
        self.boss2 = None
        self.boss_texture_list = None
        self.luch = None
        self.boss_bullet_list = None
        self.npc_list_num = None
        self.image = None
        self.texture = None
        self.engine = None
        self.engine_list = None
        self.ship_weapon = None
        self.planet = None
        self.npc_bullet = None
        self.boss_bullet = None
        self.bullet_list = None
        self.finish = None
        self.win_image = None
        self.start_image = None

        self.basic_weapon = True
        self.rocket = False
        self.start = True
        self.dialogue = True
        self.level_one = True
        self.level_two = False
        self.level_boss = False
        self.boss2_kill = False
        self.win = False

        self.boss2_health = 20
        self.npc_health = 4
        self.planet_count = 0
        self.planet_num = 0
        self.dialoge_num = 0
        self.engine_num = 0
        self.engine_count = 0
        self.weapon_num = 0
        self.weapon_rocket_num = 0
        self.weapon_count = 0
        self.weapon_rocket_count = 0
        self.k = 0
        self.b = 0
        self.set_mouse_visible(False)
        self.explosion_texture_list = []

        columns = 16
        count = 60
        sprite_width = 64
        sprite_height = 64
        file_name = "Texture/Space/Texture_villains/Destruction/PNGs/Nautolan Ship - Frigate.png"

        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

        self.explosion_asteroid_texture_list = []

        columns = 16
        count = 60
        sprite_width = 96
        sprite_height = 96
        file_name = "Texture/Space/Asteroids/Asteroid 01 - Explode.png"

        self.explosion_asteroid_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns,
                                                                       count)

        self.explosion_boss_texture_list = []

        columns = 16
        count = 60
        sprite_width = 128
        sprite_height = 128
        file_name = "Texture/Space/Texture_villains/Destruction/PNGs/Nautolan Ship - Dreadnought.png"

        self.explosion_boss_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns,
                                                                   count)

        self.sound = pygame.mixer.Sound('Texture/Space/Sound/boom.mp3')
        self.channel = pygame.mixer.Channel(0)
        self.sound_asteroid = pygame.mixer.Sound('Texture/Space/Sound/boom.wav')
        self.sound_space = pygame.mixer.Sound('Texture/Space/Sound/space.mp3')
        self.sound_laser = pygame.mixer.Sound('Texture/Space/Sound/laser.mp3')
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def setup(self):
        main_hero(self)
        space_map(self)
        self.explosions_list = arcade.SpriteList()
        self.explosions_asteroid_list = arcade.SpriteList()
        self.explosions_boss_list = arcade.SpriteList()
        self.dialoge = arcade.Sprite()
        self.ship_weapon_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()
        self.npc_bullet_list = arcade.SpriteList()
        fire_speed(self)
        self.bullet_list = arcade.SpriteList()
        self.engine_list = arcade.SpriteList()
        self.speed_npc_weapons = 0
        # Level_One
        self.npc1 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc1.center_x = 756
        self.npc1.center_y = 759
        self.npc2 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc2.center_x = 618
        self.npc2.center_y = 762
        self.npc3 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc3.center_x = 906
        self.npc3.center_y = 763
        self.npc4 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc4.center_x = 828
        self.npc4.center_y = 683
        self.npc5 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc5.center_x = 688
        self.npc5.center_y = 684
        self.npc6 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc6.center_x = 612
        self.npc6.center_y = 620
        self.npc7 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc7.center_x = 715
        self.npc7.center_y = 610
        self.npc8 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc8.center_x = 818
        self.npc8.center_y = 611
        self.npc9 = arcade.Sprite(f'Texture/Space/Texture_villains/Engine Effects/PNGs/f0.png', angle=180)
        self.npc9.center_x = 911
        self.npc9.center_y = 615
        self.npc_list_num = [self.npc1, self.npc2, self.npc3, self.npc4, self.npc5, self.npc6, self.npc7, self.npc8,
                             self.npc9]
        for i in self.npc_list_num:
            self.npc_list.append(i)
        # Level two
        self.asteroid_list = arcade.SpriteList()
        for i in range(350):
            self.asteroid = arcade.Sprite('Texture/Space/Asteroids/Asteroid 01 - Base.png')
            self.asteroid.center_x = random.randint(550, 1000)
            self.asteroid.center_y = random.randint(864, 3500)
            self.asteroid.change_y -= 2
            self.asteroid_list.append(self.asteroid)
        self.last_asteroid = arcade.Sprite('Texture/Space/Asteroids/Asteroid 01 - Base.png')
        self.last_asteroid.center_x = 10000
        self.last_asteroid.center_y = 3510
        self.last_asteroid.change_y -= 2
        self.asteroid_list.append(self.last_asteroid)
        # Boss
        self.k = 0
        self.b = 0
        self.boss_num = 0
        self.boss_count = 0
        self.boss_height = 128
        self.boss_y = 500
        self.boss_asteroid = arcade.Sprite('Texture/Space/Asteroids/Asteroid 01 - Base.png')
        self.boss_asteroid.center_x = 1900
        self.boss_asteroid.center_y = 500
        self.boss_list = arcade.SpriteList()
        self.boss1 = arcade.AnimatedTimeBasedSprite(
            'Texture/Space/Texture_villains/Weapons/PNGs/Nautolan Ship - Dreadnought - Weapons1.png', scale=1.2,
            image_x=0, image_y=0, image_width=128, image_height=128)
        self.boss1.center_x = 580
        self.boss1.center_y = 500
        if self.boss2_kill == 0:
            self.boss2 = arcade.AnimatedTimeBasedSprite(
                'Texture/Space/Texture_villains/Weapons/PNGs/Nautolan Ship - Dreadnought - Weapons1.png', scale=1.2,
                image_x=0, image_y=0, image_width=128, image_height=128)
            self.boss2.center_x = 950
            self.boss2.center_y = 500

        self.boss_list.append(self.boss1)
        self.boss_list.append(self.boss2)

        columns = 16
        count = 60
        sprite_width = 128
        sprite_height = 128
        file_name = "Texture/Space/Texture_villains/Weapons/PNGs/Nautolan Ship - Dreadnought - Weapons.png"

        self.boss_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)
        self.luch = arcade.Sprite('Texture/Space/p0.png', angle=90, scale=1.2)
        self.luch.center_x = 750
        self.luch.center_y = 500
        self.boss_bullet_list = arcade.SpriteList()
        self.planet = arcade.Sprite()
        image = 'Texture/WIN.png'
        texture = arcade.load_texture(image)
        self.win_image = arcade.Sprite()
        self.win_image.center_x = SCREEN_WIDTH // 2
        self.win_image.center_y = SCREEN_HEIGHT // 2
        self.win_image.texture = texture
        image = 'Texture/START.png'
        texture = arcade.load_texture(image)
        self.start_image = arcade.Sprite()
        self.start_image.center_x = SCREEN_WIDTH // 2
        self.start_image.center_y = SCREEN_HEIGHT // 2
        self.start_image.texture = texture

    def on_draw(self):
        if self.dialogue:
            arcade.start_render()
            arcade.draw_text('[SPACE] - start', 1360, 30, arcade.csscolor.BLACK, font_size=15,
                             font_name='Showcard Gothic')
            arcade.draw_text('[<]/[>] - dialogue', 30, 30, arcade.csscolor.BLACK, font_size=15,
                             font_name='Showcard Gothic')
            self.image = f'Texture/Space/Alter/alter{self.dialoge_num}.png'
            self.texture = arcade.load_texture(self.image)
            self.dialoge = arcade.Sprite()
            self.dialoge.center_x = 850
            self.dialoge.center_y = 450
            self.dialoge.texture = self.texture
            self.dialoge.draw()
        if self.dialogue == 0:
            arcade.start_render()
            space_map_draw(self)
            arcade.draw_text('1 - Basic', 20, 810, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
            arcade.draw_text('2 - Rocket', 20, 750, arcade.csscolor.BLACK, font_size=24, font_name='Showcard Gothic')
            if self.win:
                arcade.start_render()
                space_map_draw(self)
                self.win_image.draw()

            if self.start:
                self.start_image.draw()
            if self.start == 0:
                self.engine = arcade.AnimatedTimeBasedSprite(
                    'Texture/Space/Texture_hero/Main Ship/Main Ship - Engine Effects/PNGs/e.png',
                    scale=1,
                    image_x=self.engine_num, image_y=0, image_width=48, image_height=48)
                self.engine.center_x = self.players_sprite.center_x
                self.engine.center_y = self.players_sprite.center_y - 10
                self.engine_list = arcade.SpriteList()
                self.engine_list.append(self.engine)
                self.engine_list.draw()
                if self.level_one or self.level_two or self.level_boss:
                    if self.basic_weapon:
                        self.ship_weapon = arcade.AnimatedTimeBasedSprite(
                            'Texture/Space/Texture_hero/Main Ship/Main Ship - Weapons/'
                            'PNGs/Main Ship - Weapons - Auto Cannon.png',
                            scale=1,
                            image_x=self.weapon_num, image_y=0, image_width=48, image_height=48)
                        self.ship_weapon.center_x = self.players_sprite.center_x
                        self.ship_weapon.center_y = self.players_sprite.center_y
                        self.ship_weapon_list = arcade.SpriteList()
                        self.ship_weapon_list.clear()
                        self.ship_weapon_list.append(self.ship_weapon)
                        self.ship_weapon_list.draw()
                    if self.rocket:
                        self.ship_weapon = arcade.AnimatedTimeBasedSprite(
                            'Texture/Space/Texture_hero/Main Ship/Main Ship - Weapons/'
                            'PNGs/Main Ship - Weapons - Rockets.png',
                            scale=1,
                            image_x=self.weapon_rocket_num, image_y=0, image_width=48, image_height=48)
                        self.ship_weapon.center_x = self.players_sprite.center_x
                        self.ship_weapon.center_y = self.players_sprite.center_y + 2
                        self.ship_weapon_list.clear()
                        self.ship_weapon_list.append(self.ship_weapon)
                        self.ship_weapon_list.draw()
                    self.bullet_list.draw()
                if self.level_one:
                    self.explosions_list.draw()
                    self.npc_list.draw()
                    self.npc_bullet_list.draw()

                if self.level_two:
                    self.explosions_asteroid_list.draw()
                    self.asteroid_list.draw()

                if self.level_boss:
                    self.boss_bullet_list.draw()

                    self.boss1 = arcade.AnimatedTimeBasedSprite(
                        'Texture/Space/Texture_villains/Weapons/PNGs/Nautolan Ship - Dreadnought - Weapons1.png',
                        scale=1.2, image_x=self.b, image_y=0, image_width=128, image_height=128)
                    self.boss1.center_x = 580

                    self.boss1.center_y = 500

                    if self.boss2_kill == 0:
                        self.boss2 = arcade.AnimatedTimeBasedSprite(
                            'Texture/Space/Texture_villains/Weapons/PNGs/Nautolan Ship - Dreadnought - Weapons1.png',
                            scale=1.2, image_x=self.b, image_y=0, image_width=128, image_height=128)
                        self.boss2.center_x = 950

                        self.boss2.center_y = 500
                    if self.boss2_kill == 0:
                        self.luch.draw()
                        self.boss2.draw()
                        self.boss1.draw()
                    self.boss_asteroid.draw()
                    self.explosions_boss_list.draw()
                if self.level_one == 0 and self.level_two == 0 and self.level_boss == 0 and self.win == 0:
                    self.planet = arcade.AnimatedTimeBasedSprite(
                            'Texture/Space/planet.png',
                            scale=1.7,
                            image_x=self.planet_count, image_y=0, image_width=96, image_height=96)
                    self.planet.center_x = 769
                    self.planet.center_y = 681
                    self.planet.draw()
            main_hero_draw(self)

    def update(self, delta_time: float):
        space_map_update(self)
        self.dialoge.update()
        main_hero_update(self)
        engine_counter(self)
        weapon_counter(self)

        if self.start == 0:

            if self.basic_weapon and self.rocket == 0:
                fire_speed_update(self, 20, f'Texture/Space/Texture_hero/Main ship weapons/PNGs/w0.png', 8)
                fire_speed_draw(self)
            elif self.rocket and self.basic_weapon == 0:
                fire_speed_update(self, 50, f'Texture/Space/Texture_hero/Main ship weapons/PNGs/r0.png', 5, 1.2)
                fire_speed_draw(self, 50)
            self.bullet_list.update()
            self.engine_list.update()
            self.ship_weapon_list.update()
            if self.level_one:
                if arcade.check_for_collision_with_list(self.players_sprite, self.npc_bullet_list):
                    arcade.close_window()
                    os.system('python Space_new.py')
                for npc in self.npc_list:
                    x = random.randrange(0, 100)
                    if x == 0:
                        self.npc_bullet = arcade.Sprite(
                            f"Texture/Space/Texture_villains/Weapon Effects - Projectiles/PNGs/rn0.png", 1.2, angle=180)
                        self.npc_bullet.center_x = npc.center_x
                        self.npc_bullet.center_y = npc.center_y + 20
                        self.npc_bullet.change_y = -10
                        self.npc_bullet_list.append(self.npc_bullet)
                self.npc_bullet_list.update()
                self.npc_list.update()
                self.explosions_list.update()
                if len(self.npc_list) == 0:
                    self.level_one = False
                    self.level_two = True
            if self.win:
                with sqlite3.connect('baza.db') as con:
                    cur = con.cursor()
                    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                               sparta INTEGER,
                               space INTEGER,
                               knb INTEGER
                               )""")
                    cur.execute(
                        f"""UPDATE users SET space = 1""")
                    cur.execute("""SELECT * FROM users""")
                    con.commit()
            if self.level_two:
                if self.last_asteroid.center_y < 0:
                    self.level_one = False
                    self.level_two = False
                    self.level_boss = True
                if arcade.check_for_collision_with_list(self.players_sprite, self.asteroid_list):
                    arcade.close_window()
                    os.system('python Space_new.py')
                self.explosions_asteroid_list.update()
                self.asteroid_list.update()
            if self.level_boss:
                if arcade.check_for_collision(self.players_sprite, self.boss1) or\
                        arcade.check_for_collision(self.players_sprite, self.boss2) or\
                        arcade.check_for_collision(self.players_sprite, self.luch) or\
                        arcade.check_for_collision_with_list(self.players_sprite, self.boss_bullet_list):
                    arcade.close_window()
                    os.system('python Space_new.py')
                if self.boss2_kill:
                    self.boss_asteroid.update()
                    self.boss_asteroid.change_y -= 1
                    if self.boss_asteroid.center_y < 0:
                        self.level_one = False
                        self.level_two = False
                        self.level_boss = False
                for b in self.bullet_list:
                    if arcade.check_for_collision(self.luch, b):
                        self.bullet_list.remove(b)

                space_count(self)
                for boss in self.boss_list:
                    if self.b == 2048:
                        self.channel.play(self.sound_laser)
                    if 2048 < self.b < 3840:

                        self.boss_bullet = arcade.Sprite(
                            f"Texture/Space/Texture_villains/Weapon Effects - Projectiles/PNGs/b0.png", 1.2,
                            angle=180)

                        self.boss_bullet.center_x = boss.center_x
                        self.boss_bullet.center_y = boss.center_y - 64
                        self.boss_bullet.change_y = -10
                        self.boss_bullet_list.append(self.boss_bullet)

                self.boss_bullet_list.update()

                self.boss2.update()
                self.boss1.update()
                self.luch.update()
                self.explosions_boss_list.update()
            if self.level_one == 0 and self.level_two == 0 and self.level_boss == 0:
                planet_counter(self)

                self.planet.update()
        if arcade.check_for_collision(self.players_sprite, self.planet):
                self.start = False
                self.dialogue = False
                self.win = True
        self.players_list.update()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        main_hero_controller(self, x, y)

    def on_key_press(self, key: int, modifiers: int):
        if self.rocket:
            if key == arcade.key.KEY_1:
                self.rocket = False
                self.basic_weapon = True

        if self.basic_weapon:
            if key == arcade.key.KEY_2:
                self.basic_weapon = False
                self.rocket = True
        if self.start:
            if key == arcade.key.SPACE:
                self.start = False
                self.finish = False
        if self.dialogue:
            if key == arcade.key.SPACE:
                self.start = True
                self.dialogue = False
            if self.dialoge_num > 0:
                if key == arcade.key.LEFT:
                    self.dialoge_num -= 1

            if self.dialoge_num < 10:
                if key == arcade.key.RIGHT:
                    self.dialoge_num += 1
        if self.win:
            if key == arcade.key.ENTER:
                arcade.close_window()
                os.system('python main.py')
        if key == arcade.key.ESCAPE:
            arcade.exit()


def main():
    spacegame = Space()
    spacegame.setup()
    arcade.run()


if __name__ == "__main__":
    main()
