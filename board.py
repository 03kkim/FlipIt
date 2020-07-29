import random

class Board:
    is_highlighted = [0 for num in range(16)]
    ids = [num for num in range(16)]
    id_states = [0 for num in range(16)]
    relationships = []
    view_board = [0 for num in range(16)]

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

    def return_grid(self):
        return self.group_fours(self.view_board)

    def coords_to_id(self, x, y):
        return (y + 4 * x)

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
    def highlight(self, id):
        related_ids = self.relationships[id][id]
        self.is_highlighted.pop(id)
        self.is_highlighted.insert(id, 2)

        self.is_highlighted.pop(related_ids[0])
        self.is_highlighted.insert(related_ids[0], 3)

        self.is_highlighted.pop(related_ids[1])
        self.is_highlighted.insert(related_ids[1], 3)

    def unhighlight(self):
        self.is_highlighted = [0 for num in range(16)]

    def has_won(self):
        if not (0 in self.id_states):
            return True
        else:
            return False

    def clear_board(self):
        self.id_states = [0 for num in range(16)]
        self.view_board = self.id_states







