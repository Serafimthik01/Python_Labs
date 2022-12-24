import simple_draw as sd


def smile(x, y, color):
    start_point = sd.get_point(x, y)

    sd.circle(start_point, 50, color=sd.COLOR_DARK_GREEN, width=3)
    sd.circle(sd.get_point(x + 15, y + 20), 5, color=sd.COLOR_DARK_PURPLE, width=2)
    sd.circle(sd.get_point(x - 15, y + 20), 5, color=sd.COLOR_DARK_PURPLE, width=2)
    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x + 10, y - 25), color=sd.COLOR_DARK_RED, width=3)
    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x - 20, y - 20), color=sd.COLOR_DARK_RED, width=3)
    sd.line(sd.get_point(x + 10, y - 25), sd.get_point(x + 20, y - 20), color=sd.COLOR_DARK_RED, width=3)


if __name__ == '__main__':
    smile(x=565, y=140, color=sd.COLOR_YELLOW)