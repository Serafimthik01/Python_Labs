#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from package.tile import *
from package.wallpaper import *
from package.laminat import *
from package.save_module import *
from guizero import *

app = App("Lab10", layout="grid", height=150, width=250)
wallpaper_app = App(title="Обои", layout="grid", height=321, width=314)
tile_app = App("Плитка", layout="grid", height=310, width=340)
laminate_app = App("Ламинат", layout="grid", height=290, width=340)
wallpaper_app.hide()
tile_app.hide()
laminate_app.hide()


def back():
    wallpaper_app.hide()
    tile_app.hide()
    laminate_app.hide()
    app.show()


def exit():
    wallpaper_app.destroy()
    tile_app.destroy()
    laminate_app.destroy()
    app.destroy()


def ww():
    wallpaper_app.show()
    app.hide()
    wallpaper()


def t():
    tile_app.show()
    app.hide()
    tile()


def l():
    laminate_app.show()
    app.hide()
    laminat()


exit_Button = PushButton(app, text="Выход", command=exit, grid=[2, 1])

wallpaper_Text = Text(app, text="Обои", align="left", grid=[0, 1])
wallpaper_Button = PushButton(app, text="Начать расчет",
                              align="left", command=ww, grid=[1, 1])

tile_Text = Text(app, text="Плитка", align="left", grid=[0, 2])
tile_Button = PushButton(app, text="Начать расчет",
                         align="left", command=t, grid=[1, 2])

laminat_Text = Text(app, text="Ламинат", align="left", grid=[0, 3])
laminat_Button = PushButton(app, text="Начать расчет",
                            align="left", command=l, grid=[1, 3])


# РАСЧЕТ ОБОЕВ
def wallpaper():
    back_Button = PushButton(wallpaper_app, text="Назад",
                             align="left", command=back, grid=[0, 14])

    length_Label_Room = Text(wallpaper_app, text="Длина комнаты", grid=[0, 0])
    length_Room = TextBox(wallpaper_app, grid=[1, 0])
    length_Room.value = 0

    width_Label_Room = Text(wallpaper_app, text="Ширина комнаты", grid=[0, 1])
    width_Room = TextBox(wallpaper_app, grid=[1, 1])
    width_Room.value = 0

    height_Label = Text(wallpaper_app, text="Высота комнаты", grid=[0, 2])
    height_Room = TextBox(wallpaper_app, grid=[1, 2])
    height_Room.value = 0

    width_Label_Roll = Text(wallpaper_app, text="Ширина рулона", grid=[0, 3])
    width_Roll = TextBox(wallpaper_app, grid=[1, 3])
    width_Roll.value = 0

    length_Label_Roll = Text(wallpaper_app, text="Длина рулона", grid=[0, 4])
    length_Roll = TextBox(wallpaper_app, grid=[1, 4])
    length_Roll.value = 0

    cost_Label_Roll = Text(wallpaper_app, text="Цена рулона", grid=[0, 5])
    cost_Roll = TextBox(wallpaper_app, grid=[1, 5])
    cost_Roll.value = 0

    def W_calc_quantity():
        W_result_TextBox.value = round(calculation_quantity(float(length_Room.value), float(width_Room.value),
                                                            float(height_Room.value), float(width_Roll.value),
                                                            float(length_Roll.value)), 1)

    def W_calc_cost():
        result_cost_TextBox.value = round(calculation_cost(float(W_result_TextBox.value), float(cost_Roll.value)), 1)

    def save():
        data_Save(W_result_TextBox.value, result_cost_TextBox.value)

    result_Label = Text(wallpaper_app, text="Количество рулонов", grid=[0, 10])
    W_result_TextBox = TextBox(wallpaper_app, grid=[1, 10])
    result_Button = PushButton(wallpaper_app, text="Рассчитать", grid=[1, 11], command=W_calc_quantity)

    result_cost_Label = Text(wallpaper_app, text="Общая цена", grid=[0, 12])
    result_cost_TextBox = TextBox(wallpaper_app, grid=[1, 12])
    result_Button = PushButton(wallpaper_app, text="Рассчитать", grid=[1, 13], command=W_calc_cost)

    result_Button = PushButton(wallpaper_app, text="Сохранить результаты", grid=[1, 14], command=save)


# РАСЧЕТ ОБОЕВ


# РАСЧЕТ ПЛИТКИ
def tile():
    back_Button = PushButton(tile_app, text="Назад",
                             align="left", command=back, grid=[0, 14])

    T_length_Label_Room = Text(tile_app, text="Длина поверхности, м", grid=[0, 0])
    T_length_Room = TextBox(tile_app, grid=[1, 0])
    T_length_Room.value = 0

    T_width_Label_Room = Text(tile_app, text="Ширина поверхности, м", grid=[0, 1])
    T_width_Room = TextBox(tile_app, grid=[1, 1])
    T_width_Room.value = 0

    T_width_Label_Roll = Text(tile_app, text="Ширина плитки, см", grid=[0, 3])
    T_width_Roll = TextBox(tile_app, grid=[1, 3])
    T_width_Roll.value = 0

    T_length_Label_Roll = Text(tile_app, text="Длина плитки, см", grid=[0, 4])
    T_length_Roll = TextBox(tile_app, grid=[1, 4])
    T_length_Roll.value = 0

    T_cost_Label_Roll = Text(tile_app, text="Цена плитки", grid=[0, 5])
    T_cost_Roll = TextBox(tile_app, grid=[1, 5])
    T_cost_Roll.value = 0

    def calc_T_length():
        T_result_TextBox.value = round(T_calculation_length(float(T_length_Room.value), float(T_width_Room.value),
                                                            float(T_width_Roll.value), float(T_length_Roll.value)), 0)

    def calc_T_cost():
        T_result_cost_TextBox.value = round(T_calculation_cost(float(T_result_TextBox.value),
                                                               float(T_cost_Roll.value)), 1)

    def save():
        data_Save(0, 0, T_result_TextBox.value, T_result_cost_TextBox.value)

    T_result_Label = Text(tile_app, text="Количество плиток", grid=[0, 10])
    T_result_TextBox = TextBox(tile_app, grid=[1, 10])
    T_result_Button = PushButton(tile_app, text="Рассчитать", grid=[1, 11], command=calc_T_length)

    T_result_cost_Label = Text(tile_app, text="Общая цена", grid=[0, 12])
    T_result_cost_TextBox = TextBox(tile_app, grid=[1, 12])
    T_result_cost_Button = PushButton(tile_app, text="Рассчитать", grid=[1, 13], command=calc_T_cost)

    T_result_save_Button = PushButton(tile_app, text="Сохранить результаты", grid=[1, 14], command=save)


# РАСЧЕТ ПЛИТКИ

# РАСЧЕТ ЛАМИНТА
def laminat():
    back_Button = PushButton(laminate_app, text="Назад",
                             align="left", command=back, grid=[0, 10])

    length_Label_Room = Text(laminate_app, text="Длина комнаты", grid=[0, 0])
    length_Room = TextBox(laminate_app, grid=[1, 0])
    length_Room.value = 0

    width_Label_Room = Text(laminate_app, text="Ширина комнаты", grid=[0, 1])
    width_Room = TextBox(laminate_app, grid=[1, 1])
    width_Room.value = 0

    width_Label_Roll = Text(laminate_app, text="Площадь одной упаковки", grid=[0, 3])
    width = TextBox(laminate_app, grid=[1, 3])
    width.value = 0

    cost_Label_Roll = Text(laminate_app, text="Цена одной упаковки", grid=[0, 5])
    cost = TextBox(laminate_app, grid=[1, 5])
    cost.value = 0

    def calc_L_length():
        L_Result_TextBox.value = round(L_calculation_length(float(length_Room.value), float(width_Room.value),
                                                            float(width.value)), 1)

    def calc_L_cost():
        L_Result_cost_TextBox.value = round(L_calculation_cost(float(L_Result_TextBox.value),
                                                               float(cost.value)), 1)

    def save():
        data_Save(0, 0, 0, 0, L_Result_TextBox.value, L_Result_cost_TextBox.value)

    L_Result_Label = Text(laminate_app, text="Количество плиток", grid=[0, 6])
    L_Result_TextBox = TextBox(laminate_app, grid=[1, 6])
    L_Result_Button = PushButton(laminate_app, text="Рассчитать", grid=[1, 7], command=calc_L_length)

    L_result_cost_Label = Text(laminate_app, text="Общая цена", grid=[0, 8])
    L_Result_cost_TextBox = TextBox(laminate_app, grid=[1, 8])
    L_Result_cost_Button = PushButton(laminate_app, text="Рассчитать", grid=[1, 9], command=calc_L_cost)

    L_Result_save_Button = PushButton(laminate_app, text="Сохранить результаты", grid=[1, 10], command=save)


# РАСЧЕТ ЛАМИНТА


app.display()
