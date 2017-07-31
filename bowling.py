def isspare(result, point, last_point, max_point):
    if point == '/':
        result += max_point - last_point
    else:
        result += get_value(point)
    return result


def change_roll_and_frame(first_roll, current_frame, point):
    if first_roll:
        first_roll = False
    else:
        first_roll = True
        current_frame += 1

    if point == 'x':
        first_roll = True
        current_frame += 1
    return first_roll, current_frame


def score(game):
    result = 0
    current_frame = 1
    max_frame = 10
    max_point = 10
    first_roll = True
    for i in range(len(game)):
        result = isspare(result, game[i], get_value(game[i-1]), max_point)

        if current_frame < max_frame and game[i].lower() in "x/":
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i].lower() == 'x':
                result += get_value(game[i+1])
                result = isspare(result, game[i+2], get_value(game[i+1]), max_point)

        first_roll, current_frame = change_roll_and_frame(first_roll, current_frame, game[i].lower())
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

print(score("X34----------------"))