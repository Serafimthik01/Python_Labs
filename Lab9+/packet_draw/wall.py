import simple_draw as sd


def wall():
    v1 = sd.get_vector(start_point=sd.get_point(375, 280), angle=0, length=380, width=0)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=160, length=200, width=100)
    v2.draw(color=sd.COLOR_DARK_ORANGE)

    v3 = sd.get_vector(start_point=v2.end_point, angle=200, length=198, width=100)
    v3.draw(color=sd.COLOR_DARK_ORANGE)
    v4 = sd.get_vector(start_point=sd.get_point(755, 160), angle=180, length=375, width=320)
    v4.draw(color=sd.COLOR_DARK_ORANGE)
    line = 0
    for y in range(0, 320, 25):
        line += 1
        for x in range(380, 700, 50):
            if line % 2 == 0:
                x += 25
            left_bottom = sd.get_point(0 + x, 0 + y)
            right_top = sd.get_point(50 + x, 25 + y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_WHITE, width=2)
    v5 = sd.get_vector(start_point=sd.get_point(635, 167), angle=180, length=140, width=180)
    v5.draw(color=sd.COLOR_DARK_BLUE)


if __name__ == '__main__':
    wall()