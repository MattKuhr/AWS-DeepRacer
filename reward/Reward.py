from reward.RewardUtils import gauss
from track.TrackUtils import compute_position_in_turn, compute_distance_to_optimized_line
from track.RaceTrack import RaceTrack, TrackSector


def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    left_of_center = -1 if params['is_left_of_center'] else 1
    half_track_width = 0.5 * params['track_width']
    distance_from_center *= left_of_center

    track = RaceTrack([], True)

    sector = track.compute_track_sector(params)
    turn_position = 0
    if sector != TrackSector.STRAIGHT:
        turn_position = compute_position_in_turn(params)

    distance = compute_distance_to_optimized_line(half_track_width, distance_from_center, sector, turn_position)

    if sector == TrackSector.STRAIGHT:
        reward = compute_reward_straight(distance, half_track_width)
    else:
        reward = compute_reward_turn(distance, distance_from_center, sector, half_track_width)

    return float(reward)


def compute_reward_straight(distance_from_optimized_line, half_track_width):
    # tune the reward for being close to the center
    sigma = 0.45 * half_track_width
    return gauss(distance_from_optimized_line, 1, 0, sigma)


def compute_reward_turn(distance_from_optimized_line, distance_from_center, sector, half_track_width):
    center_reward = compute_reward_straight(distance_from_center, half_track_width)
    return center_reward







