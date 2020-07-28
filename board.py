import random
# from termcolor import colored
# import colorama
# colorama.init()

class Board:
    def __init__(self, ids=[num for num in range(16)], id_states = [0 for num in range(16)], relationships=[], view_board = [0 for num in range (16)]):
        self.ids = ids
        self.id_states = id_states
        self.relationships = relationships
        self.view_board = view_board

    # def pick_2_ids(self, id):
    #     ind1 = random.randint(0, len(self.related_ids[0]) - 1)
    #     ind2 = random.randint(0, len(self.related_ids[0]) - 1)
    #
    #     while (self.related_ids[0][ind1] == id or self.related_ids[1][ind2] == id):
    #         ind1 = random.randint(0, len(self.related_ids[0]) - 1)
    #         ind2 = random.randint(0, len(self.related_ids[0]) - 1)
    #
    #     # if they are the same, this runs until they aren't
    #     while (self.related_ids[0][ind1] == self.related_ids[1][ind2]):
    #         ind2 = random.randint(0, len(self.related_ids[0]) - 1)
    #
    #     picked_ids = [self.related_ids[0][ind1], self.related_ids[1][ind2]]
    #     self.related_ids[0].remove(picked_ids[0])
    #     self.related_ids[1].remove(picked_ids[1])
    #
    #     return picked_ids

    def front_to_back(self, list):
        list.pop(0)
        list.append(list[0])

    def split_ls_into_evens(self, ls):
        pass
    def create_relationships(self):
        id_list = [num for num in range(16)]
        rand_list1 = []
        while (len(rand_list1) < 16):
            rand_id = random.randint(0, len(id_list) - 1)
            while not (id_list[rand_id] in id_list):
                rand_id = random.randint(0, len(id_list) - 1)
                if (len(id_list) == 1):
                    rand_id = id_list[0]
                    break
            rand_list1.append(id_list[rand_id])
            id_list.remove(id_list[rand_id])


        rand_list2 = []

        for num in rand_list1:
            rand_list2.append(num)
            rand_list2.append(num)

        self.front_to_back(rand_list2)

        rand_list3 = []

        for num in range(0, 32, 2):
            temp = []
            temp.append(rand_list2[num])
            temp.append(rand_list2[num+1])
            rand_list3.append(temp)

        # randomizes ids, readies them to be put together as dictionaries with keys from self.ids
        rand_list4 = []
        while (len(rand_list4) < 16):
            rand_id = random.randint(0, len(rand_list3) - 1)
            while not (rand_list3[rand_id] in rand_list3):
                rand_id = random.randint(0, len(rand_list3) - 1)
                if (len(id_list) == 1):
                    rand_id = rand_list3[0]
                    break
            rand_list4.append(rand_list3[rand_id])
            rand_list3.remove(rand_list3[rand_id])

        for num in self.ids:
            temp_dict = {num: rand_list4[num]}
            self.relationships.append(temp_dict)



    # def create_relationships(self):
    #
    #     relationships = []
    #
    #     for num in self.ids:
    #         temp_dict = {}
    #         # temp_dict[num] = create_relationships(num)
    #
    #         relationships.append(temp_dict)
    #
    #     self.relationships = relationships


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







