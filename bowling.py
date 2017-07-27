def score(game):
    result = 0
    current_frame = 1
    max_frame = 10
    max_score = 10
    first_roll = True
    for i in range(len(game)):
        if game[i] == '/':
            result += max_score - last
        else:
            result += get_value(game[i])

        if current_frame < max_frame and get_value(game[i]) == max_score:
            if game[i].lower() == '/':
                result += get_value(game[i+1])
            elif game[i].lower() == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += max_score - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        last = get_value(game[i])

        if first_roll:
            first_roll = False
        else:
            first_roll = True
            current_frame += 1

        if game[i].lower() == 'x':
            first_roll = True
            current_frame += 1
    return result


def get_value(score):
    max_score = 10
    min_score = 0
    if score.isdigit() and (min_score < int(score) < max_score):
        return int(score)
    elif score.lower() in 'x/':
        return max_score
    elif score == '-':
        return min_score
    else:
        raise ValueError()
