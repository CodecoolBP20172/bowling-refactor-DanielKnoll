def score(points):
    result = 0
    frame = 1
    first_roll = True
    for i in range(len(points)):
        if points[i] == '/':
            result += 10 - last
        else:
            result += get_value(points[i])

        if frame < 10 and get_value(points[i]) == 10:
            if points[i] == '/':
                result += get_value(points[i+1])
            elif points[i] == 'X' or points[i] == 'x':
                result += get_value(points[i+1])
                if points[i+2] == '/':
                    result += 10 - get_value(points[i+1])
                else:
                    result += get_value(points[i+2])

        last = get_value(points[i])

        if not first_roll:
            frame += 1

        if first_roll is True:
            first_roll = False
        else:
            first_roll = True

        if points[i] == 'X' or points[i] == 'x':
            first_roll = True
            frame += 1
    return result


def get_value(point):
    if point == '1' or point == '2' or point == '3' or \
       point == '4' or point == '5' or point == '6' or \
       point == '7' or point == '8' or point == '9':
        return int(point)
    elif point == 'X' or point == 'x':
        return 10
    elif point == '/':
        return 10
    elif point == '-':
        return 0
    else:
        raise ValueError()
