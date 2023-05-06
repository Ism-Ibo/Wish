import arcade
import random


def Q(self):
    self.player_number = 1
    self.player_sprite = arcade.Sprite('Texture/KNB/KNB1.png', scale=0.5)
    self.player_sprite.center_x = 746
    self.player_sprite.center_y = 200
    self.player_list = arcade.SpriteList()
    self.player_list.append(self.player_sprite)
    self.random_npc = random.randint(1, 3)
    if self.random_npc == 1:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB5.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    elif self.random_npc == 2:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB4.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    elif self.random_npc == 3:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB6.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    if self.random_npc == 2 and self.player_number == 1 or self.random_npc == 3 and self.player_number == 2 or self.random_npc == 1 and self.player_number == 3:
        self.player_score += 1


    elif self.random_npc == 1 and self.player_number == 2 or self.random_npc == 2 and self.player_number == 3 or self.random_npc == 3 and self.player_number == 1:
        self.npc_score += 1

def W(self):
    self.player_number = 2
    self.player_sprite = arcade.Sprite('Texture/KNB/KNB2.png', scale=0.5)
    self.player_sprite.center_x = 746
    self.player_sprite.center_y = 200
    self.player_list = arcade.SpriteList()
    self.player_list.append(self.player_sprite)
    self.random_npc = random.randint(1, 3)
    if self.random_npc == 1:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB5.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    elif self.random_npc == 2:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB4.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    elif self.random_npc == 3:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB6.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    if self.random_npc == 2 and self.player_number == 1 or self.random_npc == 3 and self.player_number == 2 or self.random_npc == 1 and self.player_number == 3:
        self.player_score += 1

    elif self.random_npc == 1 and self.player_number == 2 or self.random_npc == 2 and self.player_number == 3 or self.random_npc == 3 and self.player_number == 1:
        self.npc_score += 1


def E(self):
    self.player_number = 3
    self.player_sprite = arcade.Sprite('Texture/KNB/KNB3.png', scale=0.5)
    self.player_sprite.center_x = 746
    self.player_sprite.center_y = 200
    self.player_list = arcade.SpriteList()
    self.player_list.append(self.player_sprite)
    self.random_npc = random.randint(1, 3)
    if self.random_npc == 1:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB5.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    elif self.random_npc == 2:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB4.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    elif self.random_npc == 3:
        self.npc_sprite = arcade.Sprite('Texture/KNB/KNB6.png', scale=0.5)
        self.npc_sprite.center_x = 746
        self.npc_sprite.center_y = 655
        self.npc_list = arcade.SpriteList()
        self.npc_list.append(self.npc_sprite)
    if self.random_npc == 2 and self.player_number == 1 or self.random_npc == 3 and self.player_number == 2 or self.random_npc == 1 and self.player_number == 3:
        self.player_score += 1

    elif self.random_npc == 1 and self.player_number == 2 or self.random_npc == 2 and self.player_number == 3 or self.random_npc == 3 and self.player_number == 1:
        self.npc_score += 1
