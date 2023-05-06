import arcade


def snake_update(self):
    try:
        self.npc_sprite = arcade.Sprite(f'Texture/Snake/Cacodaemon Sprite Sheet-0-0-{self.num}-0.png', scale= 1.2)
    except:
        pass
    self.npc_sprite.center_x = 1470
    self.npc_sprite.center_y = 315
    self.npc_sprite_list = arcade.SpriteList()
    self.npc_sprite_list.append(self.npc_sprite)
    self.npc_sprite_list.update()
def snake_draw(self):
    self.npc_sprite_list.draw()


def santa_update(self):

    self.santa_list.update()
def santa_draw(self):
    try:
        self.santa_sprite = arcade.Sprite(f'Texture/Santa/k{self.num}.png', scale= 1.2)
    except:
        pass
    self.santa_sprite.center_x = 1900
    self.santa_sprite.center_y = 190
    self.santa_list = arcade.SpriteList()
    self.santa_list.append(self.santa_sprite)
    self.santa_list.draw()

def Gladiator_update(self):

    self.gladiator_list.update()
def Gladiator_draw(self):
    try:
        self.gladiator_sprite = arcade.Sprite(f'Texture/Gladiator/g{self.num}.png', scale= 1.2)
    except:
        pass
    self.gladiator_sprite.center_x = 1521
    self.gladiator_sprite.center_y = 900
    self.gladiator_list = arcade.SpriteList()
    self.gladiator_list.append(self.gladiator_sprite)
    self.gladiator_list.draw()


def goblin_update(self):
    self.goblin_list.update()
def goblin_draw(self):
    try:
        self.goblin_sprite = arcade.Sprite(f'Texture/Goblin/g{self.num}.png', scale = 1.2)
    except:
        pass
    self.goblin_sprite.center_x = 1900
    self.goblin_sprite.center_y = 700
    self.goblin_list = arcade.SpriteList()
    self.goblin_list.append(self.goblin_sprite)
    self.goblin_list.draw()


def death_update(self):
    self.death_sprite = arcade.Sprite(f'Texture/Death/d{self.numd}.png', scale=0.5)
    self.death_sprite.center_x = 302
    self.death_sprite.center_y = 825
    self.death_list = arcade.SpriteList()
    self.death_list.append(self.death_sprite)
    self.death_list.update()

def death_draw(self):
    self.death_list.draw()