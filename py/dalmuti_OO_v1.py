import random
import operator

class Game(object):
    """card status, turn, prev win order"""
    def __init__(self, s = True, t = 1, w = []):
        self.status = s
        self.turn = t
        self.win_order = w
        
    
    def new_game(self):
        in_play = int(raw_input('Enter number of players. (4-8)'))
        players = []
        hands = []
        deck = Deck()
        discard = Discard()
        for i in range(in_play):
            players.append(Player(i))
            hands.append(Hand())
        deck.add()
        deck.shuffle_deck()

        hands = deck.remove(hands) #DEAL FUNCTION
        self.main(players, hands, deck, discard)
        
        
    
    def main(self, players, hands, deck, discard):
        
        
        while self.status == True:
            for p in range(len(players)):
                print discard.get_last_move()
                print hands[p]
                print ('Select a card to play.')
                in_rank = raw_input('> ')
                rank = int(in_rank)
                quant = (hands[p]).get_quant(rank)
                if len(discard.cards) == 0:
                    players[p].play(rank, quant, hands[p], discard)
                else:
                    if quant >= len(discard.get_last_move()):
                        if rank < int((discard.cards)[-1]):
                            players[p].play(rank, quant, hands[p], discard)
                        else:
                            print ('Those cards are not low enough. Try again, or pass.')
                    else:
                        print ('You do not have enough of those. Try again, or pass.')
                    self.turn += 1



class Card(object):
    """Playing card"""
    def __init__(self, rank):
        self.rank = rank
        
    def __str__(self):
        return self.rank
    
class Hand (object):
    """A hand of playing cards"""
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        
        x = []
        y = ''
        (self.cards).sort(key=operator.attrgetter('rank'), reverse=False)
        for card in self.cards:   
            y = (y + str(card.rank) + ' ')    
        return y
    
    def add(self, card):
        self.cards.append(card)
        
    def remove(self, card):
        self.cards.remove(card)
        
    def get_quant(self, selected_rank):
        """this returns a int of
        the quantity of given rank
        in players hand"""
        quant = 0
        for card in self.cards:
            if card.rank == selected_rank:
                quant += 1
        return quant
            
class Deck(Hand):
    """A list of cards that have not been dealt"""
    
    def add(self):
        for i in range(1, 13):
            for j in range(i):
                self.cards.append(Card(i))
        for i in range(2):
            self.cards.append(Card(13))
            
    def shuffle_deck(self):
        random.shuffle(self.cards)
        
    def remove(self, hands): #THIS IS THE DEAL FUNCTION
        for player_num in range(len(hands)):
            for card in range(80):
                if card % len(hands) == player_num:
                    (hands[player_num]).add(self.cards[card])
        return hands
                    
class Discard(Hand):
    """a list of played cards"""
    
    def get_last_move(self):
        """code goes here
        the code takes the last index
        until it gets to the last number
        that is the same. returns them as
        a list. for example 
        ['12', '12', '12', '11', '11', '11']
        returns ['11', '11', '11']"""
        last_move = []
        count = -1
        if len(self.cards) > 0:
            for card in self.cards:
                if (self.cards[count]).rank == (self.cards[-1]).rank:
                    last_move.append(self.cards[count])
                    count -= 1
                else:
                    return (last_move)
        else:
            print 'There are no cards down.'
            return last_move
        
class Player(object):
    """player name
    controls play() pass() and player_out()"""
    
    def __init__(self, player):
        self.player = player

        
    def __str__(self):
        return ('Player ' + str(self.player + 1))
    
    def play(self, rank, quantity, hand, discard):
        for i in range(quantity):
            for card in hand.cards:
                if card.rank == rank:
                    discard.add(card)
                    (hand.cards).remove(card)
                    break

        return

    def pass_turn(self):
        return
            
g = Game()
g.new_game()
    