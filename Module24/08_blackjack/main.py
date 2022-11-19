import random


class Card:
    def __init__(self, card_dict):
        self.suit = random.choice(list(card_dict.keys()))
        self.rang = random.choice(card_dict[self.suit])

    def score(self, card_dict):
        if self.rang not in card_dict[-4:]:
            return int(self.rang)
        elif self.rang == 'Туз':
            return 11
        else:
            return 10

    def print_card(self):
        print(self.rang, self.suit)


class Deck:
    def __init__(self):
        self.rang_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.deck = {'Червей': self.rang_deck.copy(), 'Пик': self.rang_deck.copy(), 'Крестей': self.rang_deck.copy(),
                     'Бубей': self.rang_deck.copy()}

    def pick_card(self, card_one):
        self.deck[card_one.suit].remove(card_one.rang)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = list()
        self.hand_score = 0

    def take_card(self, remaining_card, rang_deck):
        card = Card(remaining_card.deck)
        remaining_card.pick_card(card)
        self.hand.append(card)
        if self.hand[-1].rang == 'Туз' and self.hand_score >= 10:
            self.hand_score += 1
        else:
            self.hand_score += self.hand[-1].score(rang_deck)

    def print_hand(self):
        print('У {}  в руке:'.format(self.name))
        for index in range(len(self.hand)):
            self.hand[index].print_card()
        print('Очков в руке:{}\n'.format(self.hand_score))


def make_turn(player):
    while True:
        wanna_take_card = int(input('Хотите взять карту ?\n1- да \n2-нет\n'))
        if wanna_take_card == 1:
            player.take_card(deck, deck.rang_deck)
            player.print_hand()
        else:
            print('Игрок {} пасует!'.format(player.name))
            break


def win_check(player_one, player_two):
    if player_one.hand_score < 21 or player_two.hand_score < 21:
        if player_one.hand_score > player_two.hand_score:
            print('Победил {}'.format(player_one.name))
        else:
            print('Победил {}'.format(player_two.name))
    else:
        if player_one.hand_score > player_two.hand_score:
            print('Победил {}'.format(player_two.name))
        else:
            print('Победил {}'.format(player_one.name))


deck = Deck()
player_1 = Player("Ра")
player_2 = Player('Анубис')

for _ in range(2):
    player_1.take_card(deck, deck.rang_deck)
    player_2.take_card(deck, deck.rang_deck)

player_1.print_hand()
player_2.print_hand()

make_turn(player_1)
make_turn(player_2)
win_check(player_1, player_2)
