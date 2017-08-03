def score(game):
    """
    Calculates the final score of the bowling game.

    arg:
        game (str): contains all score from the game as markings ('-', 1-9, '/', 'x').

    returns:
        final score (int)
    """
    result = 0
    current_frame = 1
    max_frame = 10
    max_point = 10
    first_roll = True
    for i in range(len(game)):
        result = isspare(result, game[i], get_value(game[i-1]), max_point)
        result = calculate_extra_score(result, current_frame, max_frame, game, i, max_point)
        first_roll, current_frame = change_roll_and_frame(first_roll, current_frame, game[i].lower())
    return result


def get_value(point):
    """
    Changes the score marks into number.

    arg:
        point (srt): The marks that needs to be changed to number '-', 1-9, '/', 'x'.

    returns:
        point as a number (int)
    """
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


def isspare(result, point, last_point, max_point):
    """
    Checks if the current point is a spare, than calculates the point base for that frame.
    If not than increases the current result with the current score value.

    args:
        result (int): The sum of the scores so far.
        point (str): The current point the program is calculating.
        last_point (int): The score in the first roll before the spare.
        max_point (int): 10, the number of pins.

    returns:
        updated result (int)
    """
    if point == '/':
        result += max_point - last_point
    else:
        result += get_value(point)
    return result


def calculate_extra_score(result, current_frame, max_frame, game, i, max_point):
    """
    Checks if the current point is a spare or strike, than calculates the extra score
    from the next frame.

    args:
        result (int): The sum of the scores so far.
        current_frame (int): The current point the program is calculating.
        max_frame (int): 10, the number of frames.
        game (str): contains all score from the game as markings ('-', 1-9, '/', 'x').
        i (int): The iterator of the for loop in score function.
        max_point (int): 10, the number of pins.

    returns:
        updated result (int)
    """
    if current_frame < max_frame and game[i].lower() in "x/":
        if game[i] == '/':
            result += get_value(game[i+1])
        elif game[i].lower() == 'x':
            result += get_value(game[i+1])
            result = isspare(result, game[i+2], get_value(game[i+1]), max_point)
    return result

def change_roll_and_frame(first_roll, current_frame, point):
    """
    Changes frame value and roll value.

    args:
        first_roll (boolean): Each frame has two rolls determinates if it is the first one.
        current_frame(int): The number of frame the the program is counting at given time.
        point (str): the current score, it only matters if it is 'x'.

    returns:
        updated first_roll and current frame as a tupil.
    """
    if first_roll:
        first_roll = False
    else:
        first_roll = True
        current_frame += 1

    if point == 'x':
        first_roll = True
        current_frame += 1
    return first_roll, current_frame
