import arcade

class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__()

        self.current_texture = 0
        self.textures = texture_list

    def update(self):

        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()

    def update(self):
        self.cur_texture_index += 1
        if self.cur_texture_index < len(self.textures):
            self.texture = self.textures[self.cur_texture_index]
        else:
            self.kill()
def fire_speed(self):
    self.speed_weapons = 0

def fire_speed_draw(self, x = 20):
    if self.speed_weapons > x + 1:
        self.speed_weapons = 0



def fire_speed_update(self, x: int, spritename: str, speed, scaling = 1):
    self.speed_weapons += 1



    if self.speed_weapons == x:

        self.bullet = arcade.Sprite(
            f"{spritename}", scaling)

        self.bullet.center_x = self.players_sprite.center_x
        self.bullet.center_y = self.players_sprite.center_y + 20
        self.bullet.change_y = speed
        self.bullet_list.append(self.bullet)
    if self.level_one:
        for n in self.npc_list:



            if arcade.check_for_collision_with_list(n, self.bullet_list):
                if self.rocket == False:
                    self.npc_health -= 1
                else:
                    self.npc_health -= 2
                if self.npc_health < 0:

                    for bullet in self.bullet_list:

                        hit_list = arcade.check_for_collision_with_list(bullet, self.npc_list)

                        if len(hit_list) > 0:
                            explosion = Explosion(self.explosion_texture_list)

                            explosion.center_x = hit_list[0].center_x
                            explosion.center_y = hit_list[0].center_y

                            explosion.update()

                            self.explosions_list.append(explosion)

                            bullet.remove_from_sprite_lists()

                        for npc in hit_list:
                            self.channel.play(self.sound)
                            npc.remove_from_sprite_lists()

                        if bullet.bottom > 1920:
                            bullet.remove_from_sprite_lists()



                    self.npc_health = 4

                for b in self.bullet_list:
                    if arcade.check_for_collision(b, n):
                        self.bullet_list.remove(b)

    if self.level_two:
        for n in self.asteroid_list:

            if arcade.check_for_collision_with_list(n, self.bullet_list):

                    for bullet in self.bullet_list:

                        hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

                        if len(hit_list) > 0:
                            explosion = Explosion(self.explosion_asteroid_texture_list)

                            explosion.center_x = hit_list[0].center_x
                            explosion.center_y = hit_list[0].center_y

                            explosion.update()

                            self.explosions_asteroid_list.append(explosion)

                            bullet.remove_from_sprite_lists()

                        for asteroid in hit_list:
                            self.channel.play(self.sound_asteroid)
                            asteroid.remove_from_sprite_lists()

                        if bullet.bottom > 1920:
                            bullet.remove_from_sprite_lists()



                    for b in self.bullet_list:
                        if arcade.check_for_collision(b, n):
                            self.bullet_list.remove(b)


    if self.level_boss:
        for n in self.boss_list:

            if arcade.check_for_collision_with_list(n, self.bullet_list):
                if self.rocket == False:
                    self.boss2_health -= 1
                else:
                    self.boss2_health -= 2
                if self.boss2_health < 0:

                    for bullet in self.bullet_list:

                        hit_list = arcade.check_for_collision_with_list(bullet, self.boss_list)

                        if len(hit_list) > 0:
                            explosion = Explosion(self.explosion_boss_texture_list)

                            explosion.center_x = hit_list[0].center_x
                            explosion.center_y = hit_list[0].center_y

                            explosion.update()

                            self.explosions_boss_list.append(explosion)

                            bullet.remove_from_sprite_lists()

                        for boss in hit_list:

                            self.boss2_kill = True

                            self.channel.play(self.sound)
                            self.boss_list.clear()


                        if bullet.bottom > 1920:
                            bullet.remove_from_sprite_lists()

                    self.boss2_health = 1

                for b in self.bullet_list:
                    if arcade.check_for_collision(b, n):
                        self.bullet_list.remove(b)










class NPC(arcade.Sprite):
    def __init__(self,filename, x, y):
        super().__init__(filename=filename, center_x=x, center_y=y, angle=180, )




def space_count(self):


    if self.k != 4480:
        self.k += 32
    else:
        self.k = 0
    if self.k % 128 == 0:
        self.b += 128
    if self.b == 4480:
        self.b = 0


def planet_counter(self):
    if self.pk != 7296:
        self.pk += 24
    else:
        self.pk = 0
    if self.pk % 96 == 0:
        self.p += 96
    if self.p == 7296:
        self.p = 0









