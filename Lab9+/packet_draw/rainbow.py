import simple_draw as sd


def rainbow(point, step):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    radius = 1050
    for color in rainbow_colors:
        radius -= step
        sd.circle(center_position=point, radius=radius, color=color, width=19)


if __name__ == '__main__':
    sd.resolution = (1200, 600)
    point = sd.get_point(400, -250)
    rainbow(point=point, step=10)