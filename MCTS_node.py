from checks_counts import *
import math, copy, random

class node():
   
    def __init__(self, state, player, depth, parent = None, parent_action = None):

        self.state = state
        self.parent = parent
        self.player = player
        self.parent_action = parent_action
        self.children = []
        self.depth = depth
        self._number_of_visits = 0
        self._results = {}
        self._results[1] = 0
        self._results[-1] = 0
        self._results[0] = 0
        self._untried_actions = self.untried_actions()

    def untried_actions(self):

        self._untried_actions = get_legal_actions(self.state)
        return self._untried_actions


    def expand(self):

        action    = self._untried_actions.pop()
        new_state = copy.deepcopy(self.state)

        # Do action on new state
        new_state[action[0]][action[1]] = self.player

        child_node = node(new_state, player = 1 - self.player, depth = self.depth + 1, parent = self, parent_action = action)
        self.children.append(child_node)

        return child_node


    def _tree_policy(self):

        current_node = self
        while not current_node.is_terminal_node():

            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                # if( d < 3):
                # x = random.randint(0, len(current_node.children)-1)
                # current_node = current_node.children[x]
                # else:
                current_node = current_node.best_child()

        return current_node

    def q(self):
        wins = self._results[1]
        loses = self._results[-1]
        draws = self._results[0]
        # return 2*(wins - loses) + draws
        return wins -  loses

    def n(self):
        return self._number_of_visits

    def best_child(self, c_param = math.sqrt(2)):

        choices_weights = [(c.q() / c.n()) + c_param * math.sqrt((2 * math.log(self.n()) / c.n())) for c in self.children]
        # choices_weights = [(c.q() / c.n()) for c in self.children]

        return self.children[imax(choices_weights)]

    def is_terminal_node(self):

        if(check(self.state) == -1):
            return False

        return True

    def is_fully_expanded(self):
        return (len(self._untried_actions) == 0)


    def rollout(self):

        current_rollout_state = copy.deepcopy(self.state)
        player = copy.deepcopy(self.player)

        while not is_game_over(current_rollout_state):

            possible_moves = get_legal_actions(current_rollout_state)
            action = self.rollout_policy(possible_moves)
            current_rollout_state[action[0]][action[1]] = player
            player = 1 - player

        c = 1
        if(player == self.player):
            c = -1

        return check(current_rollout_state) * -c


    def backpropagate(self, result):

        self._number_of_visits += 1.
        self._results[result] += 1.
        if(self.parent):
            self.parent.backpropagate(-result)


    def rollout_policy(self, possible_moves):
        return possible_moves[random.randint(0, len(possible_moves)-1)]


    def best_action(self, iters = 1000):

        for i in range(iters):
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)

        return self.best_child(0)
