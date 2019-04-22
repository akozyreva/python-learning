from Cards import Cards


class Game(Cards):
    count_dict = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        'jack': 10,
        'king': 10,
        'queen': 10
    }

    def new_count(self):
        '''
        method for generating new card and counting
        '''
        result = self.random_card()
        count = result[0]
        print("count method")
        print(count)
        if count == 'ace':
            ## TODO: write logic about ace
            print("sorry, it's ace")
            pass
        else:
            return self.count_dict[count]
