import arcade
import sqlite3


def begin(self):
    arcade.draw_text('У вас очень большие потери, ваше войско измотано. Надо срочно отступать!!!', 300, 700,
                     arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text('Фиванские войска у вас на хвосте! Ваша цель:', 300, 650,
                     arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text('- Помочь войску спартанца доехать до ближайшего города. (300 км)', 300, 600,
                     arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text('- Выжить бегство Фиванских войск.', 300, 550,
                     arcade.csscolor.BLACK, font_size=20)
    self.gladiator_list.draw()


def basic():
    arcade.draw_text('1. Питьё для войск из флляги', 570, 700, arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text('2. Вперёд на умеренной скорости', 570, 650, arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text('3. Вперёд на полной скорости', 570, 600, arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text('4. Остановка на ночь', 570, 550, arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text('5. Проверка состояния', 570, 500, arcade.csscolor.BLACK, font_size=20)


def drink_water(self):
    if self.drink > 0:
        arcade.draw_text('- Вы уталили жажду своего войска', 550, 700, arcade.csscolor.BLACK, font_size=20)
        self.water_image = arcade.load_texture('Texture/TXT/d0.png')
        arcade.draw_texture_rectangle(780, 262, self.water_image.width, self.water_image.height, self.water_image, 0)
    else:
        arcade.draw_text('- В сумке закончилась вода', 590, 700, arcade.csscolor.BLACK, font_size=20)
        self.water_image = arcade.load_texture('Texture/TXT/d1.png')
        arcade.draw_texture_rectangle(780, 262, self.water_image.width, self.water_image.height, self.water_image, 0)


def slow_run(self):
    arcade.draw_text(f'- Вы проехали: {self.random_slow_miles} миль', 630, 700, arcade.csscolor.BLACK, font_size=20)
    self.wind_image = arcade.load_texture('Texture/TXT/SJbmp4a.png')
    arcade.draw_texture_rectangle(798, 400, self.wind_image.width, self.wind_image.height, self.wind_image, 0)


def fast_run(self):
    arcade.draw_text(f'- Вы проехали: {self.random_miles} миль', 630, 700, arcade.csscolor.BLACK, font_size=20)
    self.wind_image = arcade.load_texture('Texture/TXT/SJbmp4a.png')
    arcade.draw_texture_rectangle(798, 400, self.wind_image.width, self.wind_image.height, self.wind_image, 0)


def sleep(self):
    arcade.draw_text(f'- Лошади счастливы что отдохнули', 550, 700, arcade.csscolor.BLACK, font_size=20)
    self.wind_image = arcade.load_texture('Texture/TXT/s0.png')
    arcade.draw_texture_rectangle(798, 400, self.wind_image.width, self.wind_image.height, self.wind_image, 0)


def status(self):
    arcade.draw_text(f'- Пройдено миль: {self.miles}', 300, 700, arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text(f'- Напитков в сумке: {self.drink - 1}', 300, 650, arcade.csscolor.BLACK, font_size=20)
    arcade.draw_text(f'- Фиванские войска в {self.miles - self.pursuit} милях от вас', 300, 600,
                     arcade.csscolor.BLACK, font_size=20)
    self.wind_image = arcade.load_texture('Texture/TXT/28e76bad7f0f347.png')
    arcade.draw_texture_rectangle(798, 300, self.wind_image.width, self.wind_image.height, self.wind_image, 0)


def logic(self):
    if self.miles >= 300:
        with sqlite3.connect('baza.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                sparta INTEGER,
                space INTEGER,
                knb INTEGER
                )""")
            cur.execute(
                f"""UPDATE users SET sparta = 1""")
            cur.execute("""SELECT * FROM users""")
            con.commit()
        self.begin = False
        self.basic = False
        self.drink_water = False
        self.slow_run = False
        self.fast_run = False
        self.sleep = False
        self.status = False
        arcade.draw_text('Желание исполнено', 640, 602,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('Вы спасли войска Спартанца!!!', 580, 480,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('[ENTER] - back home', 680, 38,
                         arcade.csscolor.BLACK, font_size=15, font_name='Showcard Gothic')
        self.Done = True
    if 4 < self.thirst < 7:
        arcade.draw_text('Спартанцы хотят пить!!!', 20, 38, arcade.csscolor.BLACK, font_size=15)
    elif self.thirst > 6:
        self.begin = False
        self.basic = False
        self.drink_water = False
        self.slow_run = False
        self.fast_run = False
        self.sleep = False
        self.status = False
        arcade.draw_text('Игра окончена', 670, 602,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('Ваши войска пали от жажды!!!', 580, 480,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('[R] - replay', 720, 38,
                         arcade.csscolor.BLACK, font_size=15, font_name='Showcard Gothic')
        self.Done = False
    if 5 < self.fatigue < 9:
        arcade.draw_text('Лошади устали !!!', 20, 68, arcade.csscolor.BLACK, font_size=15)
    elif self.fatigue > 8:
        self.begin = False
        self.basic = False
        self.drink_water = False
        self.slow_run = False
        self.fast_run = False
        self.sleep = False
        self.status = False
        arcade.draw_text('Игра окончена', 670, 602,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('Лошади погибли, в скорем времени Фиванские войска вас дагонят!!!', 350, 438,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('[R] - replay', 720, 38,
                         arcade.csscolor.BLACK, font_size=15, font_name='Showcard Gothic')
        self.Done = False
    if self.pursuit >= self.miles:
        self.begin = False
        self.basic = False
        self.drink_water = False
        self.slow_run = False
        self.fast_run = False
        self.sleep = False
        self.status = False
        arcade.draw_text('Игра окончена', 670, 602,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('Фиванские войска догнали вас и уничтожили войска!!!', 430, 400,
                         arcade.csscolor.BLACK, font_size=20)
        arcade.draw_text('[R] - replay', 720, 38,
                         arcade.csscolor.BLACK, font_size=15, font_name='Showcard Gothic')
        self.Done = False
    elif self.miles - self.pursuit < 15:
        arcade.draw_text('Фиванские войска приближаются!!!', 20, 98, arcade.csscolor.BLACK, font_size=15)


def dealer(self):
    if self.dear == 0:
        arcade.draw_text('Вы встретили торговца!!!', 650, 30, arcade.csscolor.BLACK, font_size=15)
        self.drink = 3
        self.fatigue = 0
        self.thirst = 0
