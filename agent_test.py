"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import time

import isolation
import game_agent

from sample_players import improved_score
from importlib import reload


class TimeTracker:
    def __init__(self, length_secs=2):
        self.start_time = None
        self.length_secs = length_secs

    def restart_time(self):
        self.start_time = None

    def time_left(self):
        if not self.start_time:
            self.start_time = time.time()

        now = time.time()
        time_remaining = self.length_secs - (now - self.start_time)
        time_remaining *= 1e3
        return time_remaining if time_remaining >= 0. else 0.


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.time_tracker = TimeTracker(length_secs=10)

    def tearDown(self):
        self.time_tracker.restart_time()

    def test_minimax(self):
        board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0,
                       0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
                       1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
                       0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 26, 23]
        game = isolation.Board(self.player1, self.player2, width=7, height=7)
        game._board_state = board_state
        depth_limit = 2

        test_player = game_agent.MinimaxPlayer(search_depth=depth_limit, score_fn=improved_score)
        test_player.time_left = self.time_tracker.time_left

        best_move = test_player.minimax(game, depth=depth_limit)

        available_choices = [(6, 4)]
        # print(best_move)
        # print(game.to_string())
        self.assertTrue(best_move in available_choices)


    def test_alpha_beta(self):
        board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                       0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0,
                       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1,
                       0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 24, 14]
        game = isolation.Board(self.player1, self.player2, width=9, height=9)
        game._board_state = board_state
        depth_limit = 2

        test_player = game_agent.MinimaxPlayer(search_depth=depth_limit, score_fn=improved_score)
        test_player.time_left = self.time_tracker.time_left

        # best_move = test_player.minimax(game, depth=depth_limit)

        # expected_leaf_nodes = {((7, 2), (6, 2)), ((3, 0), (6, 2)), ((7, 0), (6, 2))}
        # print(best_move)
        # print(game.to_string())
        # self.assertTrue(best_move in available_choices)


if __name__ == '__main__':
    unittest.main()
