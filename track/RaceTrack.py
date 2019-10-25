from enum import Enum


class TrackSector(Enum):
    STRAIGHT = 0,
    TURN_LEFT = -1,
    TURN_RIGHT = 1


class RaceTrack(object):

    def __init__(self, waypoints, direction):
        self._waypoints = waypoints
        self._direction = direction

    def compute_track_sector(self, params):
        '''
        Computes whether the racer is on a Straight or a turn.
        :param params:
        :return:
        '''

        # Initially we always assume a straight for validation.
        # On a straight the optimal line is always equal to the center line.
        return TrackSector.STRAIGHT

