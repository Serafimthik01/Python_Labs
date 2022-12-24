import simple_draw as sd


root_point = sd.get_point(1100, 10)


def three(point, angle, length, delta):
    if length < 10:
        return
    color = sd.COLOR_GREEN
    if length > 30:
        color = sd.COLOR_DARK_ORANGE
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw(color=color)
    next_point = v1.end_point
    next_angle = angle + delta
    next_angle1 = angle - delta
    branch_length = sd.random_number(675, 825) / 1000
    next_length = length * branch_length

    three(point=next_point, angle=next_angle, length=next_length, delta=sd.random_number(24, 36))
    three(point=next_point, angle=next_angle1, length=next_length, delta=sd.random_number(24, 36))


if __name__ == '__main__':
    three(point=root_point, angle=90, length=100, delta=30)