import random
from termcolor import colored
import colorama
colorama.init()

class Board:
    def __init__(self, ids=[num for num in range(16)], related_ids=[[num for num in range(16)], [num for num in range(16)]], id_states = [0 for num in range (16)], relationships=[], view_board = [0 for num in range (16)]):
        self.ids = ids
        self.related_ids = related_ids
        self.id_states = id_states
        self.relationships = relationships
        self.view_board = view_board

    def pick_2_ids(self, id):
        ind1 = random.randint(0, len(self.related_ids[0]) - 1)
        ind2 = random.randint(0, len(self.related_ids[0]) - 1)

        while (self.related_ids[0][ind1] == id or self.related_ids[1][ind2] == id):
            ind1 = random.randint(0, len(self.related_ids[0]) - 1)
            ind2 = random.randint(0, len(self.related_ids[0]) - 1)

        # if they are the same, this runs until they aren't
        while (self.related_ids[0][ind1] == self.related_ids[1][ind2]):
            ind2 = random.randint(0, len(self.related_ids[0]) - 1)

        picked_ids = [self.related_ids[0][ind1], self.related_ids[1][ind2]]
        self.related_ids[0].remove(picked_ids[0])
        self.related_ids[1].remove(picked_ids[1])

        return picked_ids

    def create_relationships(self):

        relationships = []

        for num in self.ids:
            temp_dict = {}
            temp_dict[num] = self.pick_2_ids(num)

            relationships.append(temp_dict)

        self.relationships = relationships


    def group_fours(self, list):
        ls = [[], [], [], []]
        for i in range(16):
            ls[i//4].append(list[i])

        return ls

    def print_grid(self):
        ls = self.group_fours(self.view_board)
        for group in ls:
            print(group)

    def print_board(self, style):
        if (style == "grid"):
            self.print_grid()
        if (style == "line"):
            print(self.view_board)

    # flips index from 1 --> 0 or 0 --> 1
    def flip(self, id):
        if (self.id_states[id] == 0):
            self.id_states.pop(id)
            self.id_states.insert(id, 1)

        elif (self.id_states[id] == 1):
            self.id_states.pop(id)
            self.id_states.insert(id, 0)


    def switch(self, id):
        related_ids = self.relationships[id][id]
        self.flip(related_ids[0])
        self.flip(related_ids[1])

        self.view_board = self.id_states

    # highlights the selected square, prints the board in the given style, and removes the highlight after printing
    def highlight(self, id, style="grid"):
        ls_on = []
        for num in self.ids:
            if (self.id_states[num] == 1):
                ls_on.append(num)

        related_ids = self.relationships[id][id]
        self.view_board.pop(id)
        self.view_board.insert(id, 2)

        self.view_board.pop(related_ids[0])
        self.view_board.insert(related_ids[0], 3)

        self.view_board.pop(related_ids[1])
        self.view_board.insert(related_ids[1], 3)


        self.print_board(style)

        self.clear_board()
        for id in ls_on:
            self.flip(id)

    def has_won(self):
        if not (0 in self.id_states):
            return True
        else:
            return False

    def clear_board(self):
        self.id_states = [0 for num in range(16)]
        self.view_board = self.id_states







