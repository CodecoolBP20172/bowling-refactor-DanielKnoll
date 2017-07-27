def score(points):
    result = 0
    current_frame = 1
    max_frame = 10
    max_point = 10
    first_roll = True
    for i in range(len(points)):
        if points[i] == '/':
            result += max_point - last
        else:
            result += get_value(points[i])

        if current_frame < max_frame and get_value(points[i]) == max_point:
            if points[i].lower() == '/':
                result += get_value(points[i+1])
            elif points[i].lower() == 'x':
                result += get_value(points[i+1])
                if points[i+2] == '/':
                    result += max_point - get_value(points[i+1])
                else:
                    result += get_value(points[i+2])

        last = get_value(points[i])

        if not first_roll:
            current_frame += 1

        if first_roll:
            first_roll = False
        else:
            first_roll = True

        if points[i].lower() == 'x':
            first_roll = True
            current_frame += 1
    return result


def get_value(point):
    max_point = 10
    min_point = 0
    if point.isdigit() and (min_point < int(point) < max_point):
        return int(point)
    elif point.lower() in 'x/':
        return max_point
    elif point == '-':
        return min_point
    else:
        raise ValueError()
