from Game import Game


newGame = Game()
newGame.initialize_game()
game = 1
while game:
    if newGame.player_score == 21:
        print("You won! Black Jack")
        game = 0
        break
    move = int(input("Choose, what to do next - hit(1) or stand(2)? "))
    if move == 1:
        newGame.hit("player")
        if newGame.player_score == 21:
            print("You won! Black Jack")
            game = 0
        if newGame.player_score > 21:
            print("Sorry, it's over 21, you lost")
            game = 0
        else:
            pass
    else:
        # generate 2 card of dealer - it's required
        newGame.new_count('dealer')
        # sequence of movement of dealer
        dealer_turn = 1
        while dealer_turn:
            if newGame.dealer_score <= 17:
                newGame.new_count('dealer')
            else:
                if 17 <= newGame.dealer_score <= 21 and newGame.dealer_score > newGame.player_score:
                    print("Dealer won!")
                    dealer_turn = 0
                elif newGame.dealer_score == newGame.player_score:
                    print("Dead heat")
                    dealer_turn = 0
                else:
                    print("Dealer lost")
                    dealer_turn = 0
        game = 0
