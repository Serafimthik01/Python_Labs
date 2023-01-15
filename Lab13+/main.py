from calc.laminat import Laminat as lm
from calc.wallpaper import Wallpaper as wp
from calc.tile import Tile as tl
from guietta import Gui, _, Quit
from calc.save import *
from math import *

gui = Gui(
    [_, Quit, _],
    ['Обои', _, ['Расчёт']],
    ['Плитка', _, ['Расчёт']],
    ['Ламинат', _, ['Расчёт']]
)


def rasrulwp(guiwp, *args):
    length_Room = guiwp.dwp
    width_Room = guiwp.shwp
    height_Room = guiwp.vwp
    width_Roll = guiwp.shrul
    length_Roll = guiwp.drul
    cost_Roll = guiwp.tsrul
    w = wp(float(length_Room), float(width_Room), float(height_Room), float(width_Roll), float(length_Roll),
           float(cost_Roll))
    guiwp.kolrul = w.calculation_quantity()
    guiwp.tsenawp = w.calc_cost()


def closewp(guiwp, *args):
    guiwp.close()


def savewp(guiwp, *args):
    Save_Wallpaper.data_Save(guiwp.kolrul, guiwp.tsenawp)


def wpcalc(guiwp, *args):
    guiwp = Gui(
        ['Длина комнаты', '__dwp__', _],
        ['Ширина комнаты', '__shwp__', _],
        ['Высота комнаты', '__vwp__', _],
        ['Ширина рулона', '__shrul__', _],
        ['Длина рулона', '__drul__', _],
        ['Цена рулона', '__tsrul__', _],
        ['Количество рулонов', 'kolrul', _],
        ['Общая цена', 'tsenawp', _],
        [_, ['Рассчитать'], _],
        [['Назад'], _, ['Сохранить']]
    )
    guiwp.events(
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, rasrulwp, _],
        [closewp, _, savewp]
    )
    guiwp.run()


def rasplp(guitc, *args):
    length_Room = guitc.dtc
    width_Room = guitc.shtc
    width_Roll = guitc.shp
    length_Roll = guitc.pp
    cost_Roll = guitc.tsp
    t = tl(float(length_Room), float(width_Room), float(width_Roll), float(length_Roll), float(cost_Roll))
    guitc.kolp = t.calculation_quantity()
    guitc.tsenap = t.calc_cost()


def closep(guitc, *args):
    guitc.close()


def savep(guitc, *args):
    Save_Tile.data_Save(guitc.kolp, guitc.tsenap)


def tcalc(guitc, *args):
    guitc = Gui(
        ['Длина поверхности, м', '__dtc__', _],
        ['Ширина поверхности, м', '__shtc__', _],
        ['Ширина плитки, см', '__shp__', _],
        ['Длина плитки, см', '__pp__', _],
        ['Цена плитки', '__tsp__', _],
        ['Количество плиток', 'kolp', _],
        ['Общая цена', 'tsenap', _],
        [_, ['Рассчитать'], _],
        [['Назад'], _, ['Сохранить']]
    )
    guitc.events(
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, rasplp, _],
        [closep, _, savep]
    )
    guitc.run()


def raslaml(guil, *args):
    length_Room = guil.dl
    width_Room = guil.shl
    square_Lam = guil.plol
    cost = guil.tsl
    l = lm(float(length_Room), float(width_Room), float(square_Lam), float(cost))
    guil.koll = l.calculation_quantity()
    guil.tsenal = l.calc_cost()


def closel(guil, *args):
    guil.close()


def savel(guil, *args):
    Save_Laminat.data_Save(guil.koll, guil.tsenal)


def lcalc(guil, *args):
    guil = Gui(
        ['Длина комнаты', '__dl__', _],
        ['Ширина комнаты', '__shl__', _],
        ['Площадь одной упаковки', '__plol__', _],
        ['Цена одной упаковки', '__tsl__', _],
        ['Количество упаковок', 'koll', _],
        ['Общая цена', 'tsenal', _],
        [_, ['Рассчитать'], _],
        [['Назад'], _, ['Сохранить']]
    )
    guil.events(
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, raslaml, _],
        [closel, _, savel]
    )
    guil.run()


gui.events([_, _, _],
           [_, _, wpcalc],
           [_, _, tcalc],
           [_, _, lcalc]
           )

gui.run()
