import random

suits = ("Hearts","Diamonds","Clubs","Spades")
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
          "King")
values = {"Ace" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8,
          "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()



class Player:
    def __init__(self,chips):
        self.chips = chips
        self.player_cards = []
    def bet(self,bet_amt):
        while True:
            if bet_amt > self.chips:
                print("\nInvalid : Player's bet exceeds the available chips.\n")
                bet_amt = int(input("\nTry again: "))
                continue
            else:
                self.chips -= bet_amt
                break
    def profit(self,profit_amt):
        self.chips += profit_amt
    def receive(self,new_cards):
        if type(new_cards) == type([]):
            self.player_cards.extend(new_cards)
        else:
            self.player_cards.append(new_cards)
    def empty(self):
        for x in range(len(self.player_cards)):
            self.player_cards.pop()
    
class Dealer:
    def __init__(self):
        self.dealer_cards = []
    def receive(self,new_cards):
        if type(new_cards) == type([]):
            self.dealer_cards.extend(new_cards)
        else:
            self.dealer_cards.append(new_cards)
    def empty(self):
        for x in range(len(self.dealer_cards)):
            self.dealer_cards.pop()

def create_deck():    
    new_deck = Deck()
    new_deck.shuffle()
    return new_deck

def create_player():
    chips = int(input("\nEnter the value of chips that you want at the beginning: "))
    player = Player(chips)
    return player

def ask_for_bet(player):
    bet_amt = int(input("\nEnter the value that you want to bet: "))
    player.bet(bet_amt)
    return bet_amt

def hit_or_stand(player):
    opt = input("\nDo you wish to hit or stand: ")
    return opt
    

print("\nWELCOME TO THE BLACKJACK CARD GAME!!\n")
new_deck = create_deck()
player = create_player()
dealer = Dealer()
keep_playing  = True
while keep_playing :    
    bet_amt = ask_for_bet(player)
    for _ in range(2):
        player.receive(new_deck.deal_one())
        dealer.receive(new_deck.deal_one())
    print(f"\nCard with dealer : {dealer.dealer_cards[0]}\n")
    print(f"\nCards with player : {player.player_cards[0]} and {player.player_cards[1]}\n")
    game_on = True
    sum_player = player.player_cards[0].value + player.player_cards[1].value
    sum_dealer = dealer.dealer_cards[0].value + dealer.dealer_cards[1].value
    while game_on:
        
        opt = hit_or_stand(player)
        if(opt == "hit"):
            player.receive(new_deck.deal_one())
            print(f"\nNew card: {player.player_cards[-1]}\n")
            sum_player += player.player_cards[-1].value
            if(sum_player > 21):
                print("\nBUST!! You lose your money !!\n")
                break
            else:
                continue
        elif(opt == "stand"):
            while True:
                print(f"\nCards with dealer : {dealer.dealer_cards[0]} and {dealer.dealer_cards[1]}\n")
                dealer.receive(new_deck.deal_one())
                print(f"\nNew card: {dealer.dealer_cards[-1]}\n")
                sum_dealer += dealer.dealer_cards[-1].value
                
                if (sum_dealer >= 17):
                    print("\nYou win!! Your money is doubled\n")
                    player.profit(2*bet_amt)
                    game_on = False
                    break
                elif (sum_dealer > sum_player):
                    print("\nYou lose your money!!\n")
                    game_on = False
                    break
                else:
                    continue
    player.empty()
    dealer.empty()
    print(f"\nChips with you : {player.chips}\n")
    ask = input("\nDo you want to keep playing? Y or N ")
    if (ask=="Y"):
        keep_playing = True
    else:
        print("\nThank You for Playing.\n")
        keep_playing = False