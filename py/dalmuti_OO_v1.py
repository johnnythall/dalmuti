import random

class Game(object):
    """card status, turn, prev win order"""
    def __init__(self, s = True, t = 1, w = []):
        self.status = s
        self.turn = t
        self.win_order = w
        
    def main(self, players, hands, deck, discard):
        deck.add()
        deck.shuffle_deck()
        deck.remove(players)
        while self.status == True:
            for player in range(players):
                
                in_rank = raw_input('Select a card to play:')
                print('>')
                rank = int(in_rank)
                quant = Hand.get_quant(player, rank)
                if quant >= len(Discard.get_last_move):
                    if rank < int((Discard.get_last_move)[0]):
                        Player.play(rank, quant)
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
        x = ''
        for card in self.cards:
            x += str(card) + ' '
    
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
        
    def remove(self, players):
        for player_num in range(players):
            for card in range(80):
                if card % players == player_num:
                    hands[player_num].append(deck[card])
                    
class Discard(Hand):
    """a list of played cards"""
    
    def get_last_move():
        """code goes here
        the code takes the last index
        until it gets to the last number
        that is the same. returns them as
        a list. for example 
        ['12', '12', '12', '11', '11', '11']
        returns ['11', '11', '11']"""
        
class Player(object):
    """player name
    controls play() pass() and player_out()"""
    
    def __init__(self, player):
        self.player = "Player_" + str(player)
        
    def __str__(self):
        return str(self.player)
        
    def play(self, rank, quantity):
        
    