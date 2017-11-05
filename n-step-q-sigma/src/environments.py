'''
This file contains implementation of Stochastic Windy Gridworld
environments used in Multi-step Reinforcement Learning: A Unifying Algorithm
(https://arxiv.org/abs/1703.01327) paper.
'''

import gym
import gym.spaces
import numpy


class StochasticWindyGridworld(gym.Env):
    '''
    Slightly modified tabular navigation task in standard gridworld which is
    described in (Sutton & Barto, Chapter 6.5, 2017).

    Stochastic Windy Gridworld is a tabular navigation taks with Start and Goal
    states (donoted by S and G respectively) and four possible moves: right,
    left, up and down.

    When the agent moves into one of the middle columns of the grid-world, it
    is affected by an upward "wind" shifting the next state by the number of
    cells indicated below the corresponding column in the following scheme.
    Agent returns to the nearest state at the edge of the world upon being
    pushed out of the world or leaving it voluntarily.

    At the end of each time step the agent receives a constant reward of -1
    unless the Goal state is reached.

    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    S 0 0 0 0 0 0 G 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    - - - - - - - - - -
    0 0 0 1 1 1 2 2 1 0
    '''
    width = 10
    height = 7
    action_space = gym.spaces.Discrete(4)
    observation_space = gym.spaces.Discrete(width * height)
    reward_range = (-numpy.inf, 1)
    start_state = 0# coordinates_to_observation((0, 3))
    goal_state = 0# coordinates_to_observation((7, 3))

    def __init__(self):
        print('OK')

    def _step(self, action):
        pass

    def _reset(self):
        self.state = self.start_state

    def _render(self, mode, close):
        pass

    def _seed(self, seed=None):
        pass

    def coordinates_to_observation(self, coordinates):
        return coordinates[0] + coordinates[1] * self.width
