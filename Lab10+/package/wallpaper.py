# -*- coding: utf-8 -*-

def calculation_quantity(*args):
    wallpaper_strips = args[0] / (args[3] * .1)
    strips_in_one_roll = args[4] / args[2]
    # Wallpaper_strips_for_room = (args[0] / args[3]) + args[0] % args[3]#длину комнаты разделите на ширину обоев. Вы узнаете, сколько полос обоев понадобится для оклейки комнаты
    # Wallpaper_strips_from_roll =  (args[4] / args[2]) + args[4] % args[2]#длину рулона разделите на высоту комнаты. Вы узнаете, сколько полос получится из одного рулона;
    return wallpaper_strips / strips_in_one_roll


def calculation_cost(*args):
    return args[0] * args[1]

# 5.12
# 3.27
# 2.45
# 1.06
# 10
# 4500
