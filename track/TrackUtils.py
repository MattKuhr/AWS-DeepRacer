from track.RaceTrack import TrackSector

def compute_position_in_turn(params):
    '''
    Computes the position in a turn as percentage of that turn. Given a straight line between
    the two centers of the turns entrance and exit the percentage indicates how much of this line the
    racer has traveled. Since the racer won't exactly follow this straight line the point which is on a
    orthogonal line to the racer is taken.
    :param params:
    :return:
    '''
    return 0


def compute_distance_to_optimized_line(half_track_width, distance_from_center, sector, turn_position = 0):
    '''
    Computes the distance to an optimized line. The line is equal to the center line for straights.
    In tunrs it leans towards the inner point of the curve, hitting the edge at the center of the curve.

    We represent the racer being left of the line with a negative distance, so we don't have to deal with an
    extra variable tracking that.
    :param params:
    :return:
    '''

    if sector == TrackSector.STRAIGHT:
        return distance_from_center

    if turn_position < 0.5:
        linear_factor = 2 * turn_position
    else:
        linear_factor = 2 - 2 * turn_position

    new_center = linear_factor * half_track_width * 0.75 * sector

    distance_from_new_center = new_center - distance_from_center
    return distance_from_new_center