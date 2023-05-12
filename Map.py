from NPC import *


def map_setup(self):
    map_name = 'Texture/MainMap.json'
    self.title_map = arcade.load_tilemap(map_name, scaling=1)
    self.map_list_Earth = self.title_map.sprite_lists['Earth']
    self.map_list_Les = self.title_map.sprite_lists['Les']
    self.map_list_Di = self.title_map.sprite_lists['Di']
    self.map_list_Other = self.title_map.sprite_lists['Other']
    self.map_list_Sparta = self.title_map.sprite_lists['Sparta']
    self.map_list_Space1 = self.title_map.sprite_lists['Space1']
    self.map_list_Death = self.title_map.sprite_lists['Death']
    self.map_list_Stop = self.title_map.sprite_lists['Stop']

    self.physical_engine_Stop = arcade.PhysicsEngineSimple(self.player_sprite, self.map_list_Stop)


def map_draw(self):
    self.map_list_Earth.draw()
    self.map_list_Les.draw()
    self.map_list_Other.draw()
    self.map_list_Stop.draw()


def map_update(self):
    self.physical_engine_Stop.update()


def knb_map(self):
    knb_map_name = 'Texture/KNB.json'
    self.title_KNB_map = arcade.load_tilemap(knb_map_name, scaling=1)
    self.KNB_map_list1 = self.title_KNB_map.sprite_lists['1']
    self.KNB_map_list2 = self.title_KNB_map.sprite_lists['2']


def knb_map_draw(self):
    self.KNB_map_list1.draw()
    self.KNB_map_list2.draw()


def txt_map(self):
    txt_map_name = 'Texture/TXT.json'
    self.title_TXT_map = arcade.load_tilemap(txt_map_name, scaling=1)
    self.TXT_map_list1 = self.title_TXT_map.sprite_lists['1']
    self.TXT_map_list2 = self.title_TXT_map.sprite_lists['2']


def txt_map_draw(self):
    self.TXT_map_list1.draw()
    self.TXT_map_list2.draw()


def space_map(self):
    space_map_name = 'Texture/Space.json'
    self.title_Space_map = arcade.load_tilemap(space_map_name, scaling=1)
    self.Space_map_list2 = self.title_Space_map.sprite_lists['Space']
    self.Space_map_list1 = self.title_Space_map.sprite_lists['Galaxy']
    self.physical_engine_list1 = arcade.PhysicsEngineSimple(self.players_sprite, self.Space_map_list1)


def space_map_draw(self):
    self.Space_map_list2.draw()
    self.Space_map_list1.draw()


def space_map_update(self):
    self.physical_engine_list1.update()
