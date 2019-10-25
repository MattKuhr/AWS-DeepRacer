from reward.Reward import reward_function

track_width = 1.0

test_data = [
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.1, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.1, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.2, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.2, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.1, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.1, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.2, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.1, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.3, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.3, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.4, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.5, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.6, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.6, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.6, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.6, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.4, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.4, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.2, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.2, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.2, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.2, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.1, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.1, 'is_left_of_center': False, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
    {'distance_from_center': 0.0, 'is_left_of_center': True, 'track_width': track_width },
]


def test_total_reward():
    rewards = [reward_function(params) for params in test_data]
    total_reward = sum(rewards)
    print(total_reward)

test_total_reward()