class WCData:
    filename = "new_wc_data.csv"

    def __init__(self):
        self.__i = 0
        self.__data = list()
        self.__load_data()
        pass

    def __load_data(self):
        with open(self.filename, "r") as in_file:
            for line in in_file:
                new_data = line.split(",")
                new_data[-1] = new_data[-1].strip("\n")
                self.__data.append(new_data)

    def get_game(self, team_name=None):
        if team_name is None:
            if self.more_games():
                game_to_return = self.__data[self.__i]
                self.__i += 1
                return game_to_return
            else:
                return False
        else:
            if self.more_games() is False:
                return False
            next_game = self.__data[self.__i]
            self.__i += 1
            while (next_game[1] != team_name) and (next_game[3] != team_name) and (self.more_games()):
                next_game = self.__data[self.__i]
                self.__i += 1
            if (next_game[1] == team_name) or (next_game[3] == team_name):
                return next_game
            else:
                return False

    def more_games(self):
        if self.__i == len(self.__data):
            return False
        else:
            return True


class WCData_Static:

    filename = "new_wc_data.csv"

    def __init__(self):
        self.__i = 0
        self.__data = list()
        self.__load_data()
        self.__i = self.__load_i()
        pass

    def __load_i(self):
        in_file = open("WCData_Static_data.txt", 'r')
        in_line = in_file.readline()
        in_line_strip = in_line.strip("\n")
        i = int(in_line_strip)
        in_file.close()
        return i

    def __output_i(self):
        out_file = open("WCData_Static_data.txt", 'w')
        out_file.write(str(self.__i))
        out_file.close()

    def __load_data(self):
        with open(self.filename, "r") as in_file:
            for line in in_file:
                new_data = line.split(",")
                new_data[-1] = new_data[-1].strip("\n")
                self.__data.append(new_data)

    def more_games(self):
        if self.__i == len(self.__data):
            return False
        else:
            return True

    def get_game(self):
        if self.more_games():
            game_to_return = self.__data[self.__i]
            self.__i += 1
            self.__output_i()
            return game_to_return
        else:
            return False

    def reset(self):
        self.__i = 0
        self.__output_i()
